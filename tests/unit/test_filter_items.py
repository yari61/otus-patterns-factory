from __future__ import annotations
import unittest
import unittest.mock as mock

from sorting.handle.filter import FilterItems, ABCFilter


class TestCall(unittest.TestCase):
    def test_ten_items_function_called_for_each(self):
        items = [i for i in range(10)]
        func = mock.MagicMock(ABCFilter)
        handle = FilterItems(filter_func=func)
        handle(data=items)
        func.assert_has_calls([mock.call(i) for i in items], any_order=True)

if __name__ == "__main__":
    unittest.main()
