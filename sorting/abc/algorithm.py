from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

from .comparable import Comparable


class ABCAlgorithm(ABC):
    @abstractmethod
    def __call__(self, data: List[Comparable]) -> List[Comparable]:
        pass
