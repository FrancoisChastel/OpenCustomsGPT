import os
from typing import Dict

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text


DB_URI = os.environ["DB_URI"]

class ContextualTools:
    __slots__ = ("cache")

    def __init__(self, cache: Dict):
        self.cache = cache
      
    def execute_sql(self, sql_query: str) -> str:
        """Execute SQL query to reply to retrieve results of query."""
        sql_query = sql_query.replace("\t", " ")
        sql_query = sql_query.replace("\n", " ")
        engine = create_engine(DB_URI)
        with engine.connect() as connection:
            df = pd.read_sql_query(text(sql_query), connection)
            dfs = self.cache.get("sql_results")
            if dfs is None:
                dfs = []
            dfs.append(df)
            self.cache["sql_results"] = dfs
                
            if df.empty:
                return "No results found with the given query. Try to fix the query."
            else:
                if len(df) > 10:
                    return f"Trimmed only to get the first 10 df: {df.head(10).to_string()}, the complete df not displayed but accessible inside the user_session.get('sql_results')."
                else:
                    return df.to_string()
