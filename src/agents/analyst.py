
from langchain.sql_database import SQLDatabase
from sqlalchemy import create_engine, text

sql_system_prompt_template = """
### Task
Generate a SQL query to answer the [QUESTION].

### Database Schema
The query will run on a database holding importation information in a customs admistration contexte, with the following schema:
{db_schema}

Always think about filtering NULL values when needed.

Always explained your thought process and the steps you took to arrive at your solution.
"""

