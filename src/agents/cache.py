from typing import List

import pandas as pd


def init_cache():
  global cached_variables
  dataframes: List[pd.DataFrame] =[]
  cached_variables = {
    "dataframes": dataframes,
    "dataframe_counter": 0,
  }