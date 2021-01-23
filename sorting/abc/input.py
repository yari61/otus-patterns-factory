from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Any

from .comparable import Comparable


class ABCInput(ABC):
    @abstractmethod
    def read(self) -> List[Any]:
        pass
