from __future__ import annotations
from typing import List

from sorting.abc import ABCAlgorithmFactory, ABCAlgorithm, Comparable

class Selection(ABCAlgorithm):
    def __init__(self) -> None:
        pass

    def __call__(self, data: List[Comparable]):
        new_data = [i for i in data]
        for i in range(len(new_data)):
            min_idx = i
            for j in range(i+1, len(new_data)):
                if new_data[min_idx] > new_data[j]:
                    min_idx = j
            new_data[i], new_data[min_idx] = new_data[min_idx], new_data[i]
        return new_data


class SelectionFactory(ABCAlgorithmFactory):
    def __init__(self) -> None:
        pass

    def create(self) -> Selection:
        return Selection()
