from __future__ import annotations
import unittest

from sorting.algorithms.insertion import Insertion


class TestCall(unittest.TestCase):
    def test_ten_items_sorted_correctly(self):
        items = [i for i in range(10, 0, -1)]
        expected = sorted(items)
        algorithm = Insertion()
        sorted_items = algorithm(data=items)
        self.assertEqual(expected, sorted_items)

if __name__ == "__main__":
    unittest.main()
