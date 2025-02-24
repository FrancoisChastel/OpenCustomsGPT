# Copyright (C) Francois Chastel - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Francois Chastel <francois@chastel.co>, February 2024
from typing import List

import pandas as pd


def init_cache():
  global cached_variables
  dataframes: List[pd.DataFrame] =[]
  cached_variables = {
    "dataframes": dataframes,
    "dataframe_counter": 0,
  }  
