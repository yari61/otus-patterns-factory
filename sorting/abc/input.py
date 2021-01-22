from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

from .comparable import Comparable


class ABCInput(ABC):
    @abstractmethod
    def read(self) -> List[Comparable]:
        pass
