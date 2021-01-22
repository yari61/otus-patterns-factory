from __future__ import annotations
from os import PathLike
from typing import List, Any

from sorting.abc import ABCOutput, Comparable


class FileOutput(ABCOutput):
    __slots__ = ("_path",)

    def __init__(self, path: PathLike):
        self._path = path

    def write(self, data: List[Comparable]) -> None:
        with open(self._path, mode="w") as file:
            for item in data:
                file.write(item + "\n")
