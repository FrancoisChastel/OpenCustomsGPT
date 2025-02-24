import json
import os
import pickle
import uuid
from enum import Enum
from pathlib import Path
from typing import Any
from typing import List
from typing import cast

import pandas as pd
import streamlit as st
from attr import dataclass
from plotly.graph_objs import Figure
from sqlalchemy import create_engine
from sqlalchemy import text
from streamlit.elements.plotly_chart import FigureOrData

from agents import cache
from agents.setup import EXECUTION_WORK_DIR


DB_URI = os.environ["DB_URI"]


class FunctionResult(Enum):
    FAILED = "FAILED"
    SUCCESS = "SUCCESS"
    NO_RESULT = "NO_RESULT"

class OutputType(Enum):
    SQL = "SQL"
    PLOT = "PLOT"
    DATAFRAME = "DATAFRAME"
    PICKLED_DATAFRAME = "PICKLED_DATAFRAME"
    UNKNOWN = "UNKNOWN"

class VisualizationLibrary(Enum):
    PLOTLY = "plotly"

def serialize_variables(variables: List[Any]) -> str:
    """Serialize results to JSON."""
    results = []
    for variable in variables:
        results.append(serialize_variable(variable))
    return json.dumps(results)

def serialize_variable(variable: Any) -> dict:
    """Serialize results to JSON."""
    cache.cached_variables["counter"] += 1
    path = Path(EXECUTION_WORK_DIR) / f"var_{cache.cached_variables['counter']}.pkl"
    relative_path = path.relative_to(EXECUTION_WORK_DIR)

    if isinstance(variable, pd.DataFrame):
        variable.to_pickle(path)
        result = {
            "file_path": str(relative_path),
            "output_type": OutputType.PICKLED_DATAFRAME.value,
            "row_counts": variable.shape[0],
            "columns": variable.columns.tolist(),
        }
    elif isinstance(variable, Figure):
        with open(path, "wb") as f:
            pickle.dump(variable, f)
        result = {
            "file_path": str(relative_path),
            "output_type": OutputType.PLOT.value,
            "library": VisualizationLibrary.PLOTLY.value,
        }
    else:
        result = {
            "message": "Unknown variable type",
            "output_type": OutputType.UNKNOWN.value,
        }
    return result


# Example of data interaction using tool calling
def execute_sql(sql_query: str) -> str:
    """Execute SQL query and retrieve results."""
    sql_query = " ".join(sql_query.split())
    engine = create_engine(DB_URI)
    
    with engine.connect() as connection:
        df = pd.read_sql_query(text(sql_query), connection)
        
    cache.cached_variables["dataframes"].append(df)
    cache.cached_variables["dataframe_counter"] += 1
    df_file_path = Path(EXECUTION_WORK_DIR) / f"df_{cache.cached_variables['dataframe_counter']}.pkl"
    df.to_pickle(df_file_path)
    
    if df.empty:
        return json.dumps([{"message": "No data found", "result": FunctionResult.NO_RESULT.value}])
    
    relative_df_file_path = df_file_path.relative_to(EXECUTION_WORK_DIR)
    
    return json.dumps([{
        "message": "Data are accessible from the dataframe at the path provided in a pickled file",
        "variables": {
            "file_path": str(relative_df_file_path),
            "columns": df.columns.tolist(),
            "output_type": OutputType.PICKLED_DATAFRAME.value
        },
        "result": FunctionResult.SUCCESS.value
    }])      
