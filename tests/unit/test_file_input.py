from __future__ import annotations
import unittest
import unittest.mock as mock
from os import PathLike

from sorting.input.file import FileInput


class TestRead(unittest.TestCase):
    def test_correct_file_opened(self):
        with mock.patch("sorting.input.file.open") as open:
            path = mock.Mock(PathLike)
            input = FileInput(path=path)
            input.read()
            open.assert_called_once_with(path, mode="r")

if __name__ == "__main__":
    unittest.main()
