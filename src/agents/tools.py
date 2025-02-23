import os

import pandas as pd
import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy import text

from agents import cache


DB_URI = os.environ["DB_URI"]

      
def execute_sql(sql_query: str) -> str:
    """Execute SQL query to reply to retrieve results of query."""
    sql_query = sql_query.replace("\t", " ")
    sql_query = sql_query.replace("\n", " ")
    engine = create_engine(DB_URI)
    with engine.connect() as connection:
        df = pd.read_sql_query(text(sql_query), connection)
        dfs = cache.cached_variables.get("dataframes")
        if dfs is None:
            dfs = []
        dfs.append(df)            
        cache.cached_variables["dataframes"] = dfs

        if df.empty:
            return "No results found with the given query. Try to fix the query."
        else:
            if len(df) > 10:
                return f"Trimmed only to get the first 10 df: {df.head(10).to_string()}, the complete df not displayed but accessible inside the df in the cache, all agents can use it."
            else:
                return df.to_markdown()
