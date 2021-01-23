from __future__ import annotations
import unittest

from sorting.algorithms.selection import Selection


class TestCall(unittest.TestCase):
    def test_ten_items_sorted_correctly(self):
        items = [i for i in range(10, 0, -1)]
        expected = sorted(items)
        algorithm = Selection()
        sorted_items = algorithm(data=items)
        self.assertEqual(expected, sorted_items)

if __name__ == "__main__":
    unittest.main()
