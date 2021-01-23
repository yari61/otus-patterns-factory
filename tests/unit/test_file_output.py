from __future__ import annotations
import unittest
import unittest.mock as mock
from os import PathLike
from typing import List

from sorting.output.file import FileOutput


class TestRead(unittest.TestCase):
    def test_correct_file_opened(self):
        with mock.patch("sorting.output.file.open") as open:
            path = mock.Mock(PathLike)
            data = mock.MagicMock(list)
            output = FileOutput(path=path)
            output.write(data=data)
            open.assert_called_once_with(path, mode="w")

if __name__ == "__main__":
    unittest.main()
