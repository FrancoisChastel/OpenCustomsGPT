
from langchain.sql_database import SQLDatabase
from sqlalchemy import create_engine
from sqlalchemy import text

from agents.sql_info import SAD_GEN_SCHEMA
from agents.sql_info import SAD_ITEM_SCHEMA


sql_system_prompt_template = """
### Task
Generate a SQL query to answer the question. You only generate the query.
You never generate user <tool_response> results.

### Database Schema
The query that you will generate run on a database holding importation information in a customs admistration contexte, with the following schema:
{db_schema}

The query MUST be run by SQL_Executor, you can't execute it your only role is to provide the sql query to be executed.
Never come up with a solution that requires changing the schema or inserting data.
Never come up with fake data.
You never fakely execute the sql query by yourself. only SQL_Executor can have the output of the query.
You never run the sql query by yourself. only SQL_Executor can have the output of the query.
You never provide the data to Data_Analyst, only SQL_Coder can provide the data to Data_Analyst.
When you have errors or empty results try give an explanation to what could be wrong.
You should always ask SQL_Executor to run the query to come up with data.
"""

sql_fix_prompt_template = """
You give suggestion on how to fix the query that may fail.

You should trust the schema used by SQL_Coder.
You should never suggest to change the schema or insert data.
You try to give a thought process more than an actual definitive solution.

Always explained your thought process and the steps you took to arrive at a solution.
"""


def create_db(postgresql_uri: str) -> SQLDatabase:
    return SQLDatabase(create_engine(postgresql_uri), schema="sydonia")

def get_sql_system_prompt(db_schema: str) -> str:
    return sql_system_prompt_template.format(db_schema=db_schema)

def get_sql_fix_system_prompt(db_schema: str) -> str:
    return sql_fix_prompt_template.format(db_schema=db_schema)


def get_schema() -> str:
    return f"{SAD_GEN_SCHEMA}\n{SAD_ITEM_SCHEMA}" 

def get_schema() -> str:
    return f"{SAD_GEN_SCHEMA}\n{SAD_ITEM_SCHEMA}" 