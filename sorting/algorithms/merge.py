from __future__ import annotations
from typing import List

from sorting.abc import ABCAlgorithmFactory, ABCAlgorithm, Comparable

class Merge(ABCAlgorithm):
    def __init__(self) -> None:
        pass

    def __call__(self, data: List[Comparable]) -> List[Comparable]:
        new_data = [i for i in data]
        self._merge_sort(new_data)
        return new_data

    def _merge_sort(self, data: List[Comparable]) -> None:
        if len(data) > 1:
            mid = len(data)//2
            L = data[:mid]
            R = data[mid:]
            self._merge_sort(L)
            self._merge_sort(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    data[k] = L[i]
                    i += 1
                else:
                    data[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                data[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                data[k] = R[j]
                j += 1
                k += 1


class MergeFactory(ABCAlgorithmFactory):
    def __init__(self) -> None:
        pass

    def create(self) -> Merge:
        return Merge()
