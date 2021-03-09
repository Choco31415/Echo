"""
Imports and holds the conf file. Nothing else.
"""
# Handle imports
import configparser

# Define values
conf_file = "Resources/conf.ini"

# Run code
config = configparser.ConfigParser()
config.read(conf_file)