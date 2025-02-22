
from agents.prompts import SQL_CODER_PROMPT
from agents.schema import SAD_GEN_SCHEMA
from agents.schema import SAD_ITEM_SCHEMA


def get_sql_coder_prompt() -> str:
    return SQL_CODER_PROMPT.format(db_schema=get_schema())

def get_schema() -> str:
    return f"{SAD_GEN_SCHEMA}\n{SAD_ITEM_SCHEMA}" 
