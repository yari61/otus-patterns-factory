from __future__ import annotations
from typing import List

from sorting.abc import ABCAlgorithmFactory, ABCAlgorithm, Comparable

class Insertion(ABCAlgorithm):
    def __init__(self) -> None:
        pass

    def __call__(self, data: List[Comparable]) -> List[Comparable]:
        new_data = [i for i in data]
        for i in range(1, len(new_data)): 
            key = new_data[i]
            j = i-1
            while j >=0 and key < new_data[j]:
                    new_data[j+1] = new_data[j]
                    j -= 1
            new_data[j+1] = key
        return new_data


class InsertionFactory(ABCAlgorithmFactory):
    def __init__(self) -> None:
        pass

    def create(self) -> Insertion:
        return Insertion()
