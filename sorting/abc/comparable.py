from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import Any

class Comparable(metaclass=ABCMeta):
    @abstractmethod
    def __lt__(self, other: Any) -> bool:
        pass
