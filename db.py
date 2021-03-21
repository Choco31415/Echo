"""
Handles the basic db operations
"""
# Imports
import sqlite3

# Variables

# Functions
def get_db(location):
    db = sqlite3.connect(
        location,
        detect_types=sqlite3.PARSE_DECLTYPES
    )
    db.row_factory = sqlite3.Row

    return db

def close_db(db):
    db.close()

def init_db(location, schema_file):
    db = get_db(location)

    with open(schema_file, 'r') as f:
        db.executescript(f.read())