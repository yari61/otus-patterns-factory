from __future__ import annotations
from abc import ABC, abstractmethod

from .algorithm import ABCAlgorithm


class ABCAlgorithmFactory(ABC):
    def create(self) -> ABCAlgorithm:
        pass
