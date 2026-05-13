from .exceptions import BaseExceptionHandler, noop
from collections.abc import Callable 
import logging

# Exception class for handling errors in a graceful way.
class ExceptionsLoggerHandler(BaseExceptionHandler):
    # The constructor initializes the logger and sets up the file to write
    def __init__(
        self,
        name: str,
    ):
        self.logger = logging.getLogger(name) # creates a local logger
        
        # creates file handler and set level to ERROR
        file_handler = logging.FileHandler(f'{name}.log')
        file_handler.setLevel(logging.ERROR)

        # creates a format for the logger
        formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
        file_handler.setFormatter(formatter)

        # sets the file handler to the logger
        self.logger.addHandler(file_handler)

    # Handles the error so no exception is thrown but is logged to a file
    # in case an error is raised in the execute callback the onError callback is called and no error is raised
    # in case everything is ok the onSuccess callback is called
    def handle(
        self,
        execute: Callable, 
        onSuccess: Callable = noop, 
        onError: Callable = noop
    ):
        try:
            execute()
        except Exception as exception:
            onError()
            self.log_error(exception)
        else:
            onSuccess()

    # Logs the error to the file
    def log_error(
        self,
        error: Exception
    ):
        self.logger.error(error)
        
