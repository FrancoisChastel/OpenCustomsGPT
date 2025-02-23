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
    path = f"var_{uuid.uuid4()}.pkl"

    if isinstance(variable, pd.DataFrame):
        variable.to_pickle(path)
        result = {
            "path": str(path),
            "output_type": OutputType.PICKLED_DATAFRAME.value,
            "row_counts": variable.shape[0],
            "columns": variable.columns.tolist(),
        }
    elif isinstance(variable, Figure):
        with open(path, "wb") as f:
            pickle.dump(variable, f)
        result = {
            "path": str(path),
            "output_type": OutputType.PLOT.value,
            "library": VisualizationLibrary.PLOTLY.value,
        }
    else:
        result = {
            "message": "Unknown variable type",
            "output_type": OutputType.UNKNOWN.value,
        }
    return result
    return result
