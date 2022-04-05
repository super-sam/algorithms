from abc import ABC, abstractmethod
from typing import Any

class QueueAbstract(ABC):
    @abstractmethod
    def get(self) -> Any:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def enque(self, item: Any) -> None:
        pass

    @abstractmethod
    def deque(self) -> Any:
        pass
