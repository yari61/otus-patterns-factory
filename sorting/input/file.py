from __future__ import annotations
from os import PathLike
from typing import List, Any

from sorting.abc import ABCInput


class FileInput(ABCInput):
    __slots__ = ("_path",)

    def __init__(self, path: PathLike):
        self._path = path

    def read(self) -> List[str]:
        with open(self._path, mode="r") as file:
            content = file.read()
        data = content.split("\n")
        return data
