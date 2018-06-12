import unittest

from score import calculate_points


class CalculatePointsTestCase(unittest.TestCase):

    def setUp(self):
        self.grid = [[0 for _ in range(3)] for _ in range(3)]

    def test_points(self):
        self.grid[0][0] = 1
        self.assertEqual(calculate_points(self.grid, 1, 0), 0)
        self.grid[0][2] = 1
        self.assertEqual(calculate_points(self.grid, 1, 0), 3)
        self.grid[0][1] = 1
        self.assertEqual(calculate_points(self.grid, 0, 1), 2)


if __name__ == '__main__':
    unittest.main()