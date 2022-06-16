import unittest
from main import check_overlap
from box import Box


class OverlapTestCase(unittest.TestCase):
    def test_not_overlap_top_left(self):
        self.assertEqual(check_overlap(Box(0, 0, 1, 1), Box(10, 10, 10, 10)), False)

    def test_not_overlap_top_center(self):
        self.assertEqual(check_overlap(Box(12, 0, 1, 1), Box(10, 10, 10, 10)), False)

    def test_not_overlap_top_right(self):
        self.assertEqual(check_overlap(Box(22, 0, 1, 1), Box(10, 10, 10, 10)), False)

    def test_not_overlap_left_center(self):
        self.assertEqual(check_overlap(Box(0, 12, 1, 1), Box(10, 10, 10, 10)), False)

    def test_not_overlap_right_center(self):
        self.assertEqual(check_overlap(Box(22, 12, 1, 1), Box(10, 10, 10, 10)), False)

    def test_not_overlap_bottom_left(self):
        self.assertEqual(check_overlap(Box(0, 22, 1, 1), Box(10, 10, 10, 10)), False)

    def test_not_overlap_bottom_center(self):
        self.assertEqual(check_overlap(Box(12, 22, 1, 1), Box(10, 10, 10, 10)), False)

    def test_not_overlap_bottom_right(self):
        self.assertEqual(check_overlap(Box(22, 22, 1, 1), Box(10, 10, 10, 10)), False)

    def test_overlap_inside(self):
        self.assertEqual(check_overlap(Box(12, 12, 1, 1), Box(10, 10, 10, 10)), True)

    def test_overlap_full_cover(self):
        self.assertEqual(check_overlap(Box(0, 0, 25, 25), Box(10, 10, 10, 10)), True)

    def test_partly_overlap_top_left(self):
        self.assertEqual(check_overlap(Box(0, 0, 15, 15), Box(10, 10, 10, 10)), True)

    def test_partly_overlap_top_center(self):
        self.assertEqual(check_overlap(Box(12, 0, 5, 15), Box(10, 10, 10, 10)), True)

    def test_partly_overlap_top_right(self):
        self.assertEqual(check_overlap(Box(12, 0, 15, 15), Box(10, 10, 10, 10)), True)

    def test_partly_overlap_top_half(self):
        self.assertEqual(check_overlap(Box(0, 0, 25, 15), Box(10, 10, 10, 10)), True)

    def test_partly_overlap_left_half(self):
        self.assertEqual(check_overlap(Box(0, 0, 15, 25), Box(10, 10, 10, 10)), True)

    def test_partly_overlap_right_half(self):
        self.assertEqual(check_overlap(Box(15, 0, 15, 15), Box(10, 10, 10, 10)), True)

    def test_partly_overlap_bottom_half(self):
        self.assertEqual(check_overlap(Box(0, 15, 25, 15), Box(10, 10, 10, 10)), True)


if __name__ == '__main__':
    unittest.main()
