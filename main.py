import os
from postgres_da_ai_agent.modules.db import PostgresManager
from postgres_da_ai_agent.modules import llm
import dotenv
import argparse

def main():

    print(f"Hello, world!")
    # list of what main will do:
        # parse prompt rapameter using arg parse
        #  connect to db using with statement and create a db_manager
        #  call db_manager.get_table_Definetion_for_Prompt() to get tables in proimpt ready form
        # create 2 blank calls to llm.app_cap_ref() taht update our current prompt passewd in from cli
        # parse sql response from prompt_reponse using SQL_QUERY_DELIMTER '___________'
        # call db_manager.run_sql() with parsed sql

    # pass

if __name__ == '__main__':
    main()