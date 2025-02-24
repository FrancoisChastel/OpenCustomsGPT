import os

from agents.prompts import SQL_CODER_PROMPT


def get_sql_coder_prompt() -> str:
    return SQL_CODER_PROMPT.format(db_schema=get_schema())

def get_schema() -> str:
    schema_path = os.path.join(os.path.dirname(__file__), "../data_schema/tmp/schema.txt")
    with open(schema_path, "r") as f:
        schema = f.read()
    return schema
