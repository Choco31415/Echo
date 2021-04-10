"""
Define the logging setup.

Note: Done in code so as to separate login details
"""
# Define imports
import logging
import logging.handlers as handlers
import sys

from config import config

# Define vars
log_file = "Logs/Log.out"

# Define functions
def get_simple_formatter():
    return logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s : %(message)s",
                             datefmt='%m/%d %I:%M:%S %p')

def get_console_handler():
    """
    Console handler. Easy
    :return:
    """
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(get_simple_formatter())
    return console_handler

def get_file_handler():
    """
    Basic file handler for 1 months worth of logs
    :return:
    """
    file_handler = handlers.TimedRotatingFileHandler(log_file, 'midnight', 1, 30)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(get_simple_formatter())
    return file_handler

def get_email_handler():
    """
    SMTP email handler in case of errors.
    :return:
    """
    mailhost = config["email"]["mailhost"]
    username = config["email"]["login username"]
    password = config["email"]["login password"]
    toaddr = config["email"]["to address"]

    email_handler = handlers.SMTPHandler(mailhost=mailhost,
                                         fromaddr=username,
                                         toaddrs=[toaddr],
                                         subject="Echo Error Log",
                                         credentials=(username, password),
                                         secure=())
    email_handler.setLevel(logging.ERROR)
    email_handler.setFormatter(get_simple_formatter())
    return email_handler

def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    logger.addHandler(get_email_handler())
    logger.propagate = False
    return logger

# Setup logs
logger = get_logger("echo")