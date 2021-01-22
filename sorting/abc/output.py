from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

from .comparable import Comparable


class ABCOutput(ABC):
    @abstractmethod
    def write(self, data: List[Comparable]) -> None:
        pass
