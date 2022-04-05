from abc import ABC, abstractmethod
from typing import Any


class StackAbstract(ABC):
    @abstractmethod
    def is_empty(self)-> bool:
        pass

    @abstractmethod
    def peek(self) -> Any:
        pass

    @abstractmethod
    def pop(self) -> Any:
        pass

    @abstractmethod
    def push(self, item: Any) -> None:
        pass
