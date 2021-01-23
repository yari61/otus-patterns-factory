from __future__ import annotations
import unittest
import unittest.mock as mock

from sorting.algorithms.selection import SelectionFactory


class TestCreate(unittest.TestCase):
    def test_correct_object_created(self):
        with mock.patch("sorting.algorithms.selection.Selection") as algorithm_class:
            factory = SelectionFactory()
            algorithm = factory.create()
            self.assertEqual(algorithm, algorithm_class())

if __name__ == "__main__":
    unittest.main()
