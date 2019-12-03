import unittest
from mapwork.map import map


class TestMap(unittest.TestCase):

    def test_valid_neighbors(self):
        self.assertEqual([(1, 0), (2, 1), (1, 2), (0, 1)], map.valid_neighbors((1, 1), 5, 5))
        # checking for "out of bounds"
        self.assertEqual([(1, 0), (0, 1)], map.valid_neighbors((0, 0), 5, 5))
        self.assertEqual([(4, 3), (3, 4)], map.valid_neighbors((4, 4), 5, 5))


if __name__ == '__main__':
    unittest.main()
