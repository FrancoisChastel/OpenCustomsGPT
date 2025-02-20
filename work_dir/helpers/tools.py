# Copyright (C) 2025 Francois Chastel
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.


import json
import os
import pickle
import uuid
from enum import Enum
from typing import Any
from typing import List

import pandas as pd
from plotly.graph_objs import Figure


DB_URI = os.environ["DB_URI"]

class FunctionResult(Enum):
    FAILED = "FAILED"
    SUCCESS = "SUCCESS"
    NO_RESULT = "NO_RESULT"

class OutputType(Enum):
    SQL = "SQL"
    PLOT = "PLOT"
    STRING = "STRING"
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
            "file_path": str(path),
            "output_type": OutputType.PICKLED_DATAFRAME.value,
            "row_counts": variable.shape[0],
            "columns": variable.columns.tolist(),
            "first_10_rows": variable.head(10).to_dict(),
        }
    elif isinstance(variable, pd.Series):
        variable = variable.to_frame()
        variable.to_pickle(path)
        result = {
            "file_path": str(path),
            "output_type": OutputType.PICKLED_DATAFRAME.value,
            "row_counts": variable.shape[0],
            "columns": variable.columns.tolist(),
            "first_10_rows": variable.head(10).to_dict(),
        }
    elif isinstance(variable, str):
        result = {
            "value": variable,
            "output_type": OutputType.STRING.value,
        }        
    elif isinstance(variable, Figure):
        with open(path, "wb") as f:
            pickle.dump(variable, f)
        result = {
            "file_path": str(path),
            "output_type": OutputType.PLOT.value,
            "library": VisualizationLibrary.PLOTLY.value,
        }
    else:
        result = {
            "message": "Unknown variable type, only pandas DataFrame, Series and plotly Figure are supported",
            "output_type": OutputType.UNKNOWN.value,
        }
    return result
