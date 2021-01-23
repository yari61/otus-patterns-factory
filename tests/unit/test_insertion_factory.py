from __future__ import annotations
import unittest
import unittest.mock as mock

from sorting.algorithms.insertion import InsertionFactory


class TestCreate(unittest.TestCase):
    def test_correct_object_created(self):
        with mock.patch("sorting.algorithms.insertion.Insertion") as algorithm_class:
            factory = InsertionFactory()
            algorithm = factory.create()
            self.assertEqual(algorithm, algorithm_class())

if __name__ == "__main__":
    unittest.main()
