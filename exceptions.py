from abc import ABC, abstractmethod
from collections.abc import Callable

# for empty function that does nothing
noop = lambda: None

# abstract class for creating exception handlers
class BaseExceptionHandler(ABC):
    @abstractmethod
    def handle(
        self, 
        execute: Callable, 
        onSuccess: Callable = noop, 
        onError: Callable = noop
    ):
        """This method should be implemented for handling errors"""
        pass