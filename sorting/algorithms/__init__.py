from sorting.abc import ABCAlgorithm, ABCAlgorithmFactory

from .merge import MergeFactory
from .insertion import InsertionFactory
from .selection import SelectionFactory


class Container:
    factories = {
        "insertion": InsertionFactory,
        "merge": MergeFactory,
        "selection": SelectionFactory
    }

    def algorithm(self, key: str) -> ABCAlgorithm:
        return self.factory(key=key).create()
    
    def factory(self, key: str) -> ABCAlgorithmFactory:
        return self.factories[key]()

__all__ = ["Container"]
