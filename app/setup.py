"""
This file is to be run on project setup only.

Rerunning it will result in a loss of data.
"""
# Handle imports
from db import init_db
from config import db_file, schema_file

# Define vars

# Run code
print("Running this command will setup the bot for use.")
print("It will also result in the loss of existing data.")
answer = input("Do you wish to continue? (Y/N) ")

if answer.lower() == "y":
    init_db(db_file, schema_file)
    print("The project is setup.")
else:
    print("Code aborted.")