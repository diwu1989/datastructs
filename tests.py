import unittest

from bit import BinaryIndexedTree
from st import SegmentTree


class BinaryIndexedTreeTest(unittest.TestCase):

    def test_instantiation(self):
        BinaryIndexedTree(range(10))
        BinaryIndexedTree([])
        BinaryIndexedTree(range(-10, 10, 1))
        BinaryIndexedTree([1])
        BinaryIndexedTree([-1, 0, 1, 0, -1, 0, 1])

    def test_prefix_sum(self):
        t = BinaryIndexedTree(range(100))
        self.assertEqual(t.prefix_sum(0), 0)
        self.assertEqual(t.prefix_sum(10), 55)
        self.assertEqual(t.prefix_sum(13), 91)
        self.assertEqual(t.prefix_sum(99), 4950)

        t = BinaryIndexedTree([-1, 1, 0, 1, -1])
        self.assertEqual(t.prefix_sum(0), -1)
        self.assertEqual(t.prefix_sum(1), 0)
        self.assertEqual(t.prefix_sum(2), 0)
        self.assertEqual(t.prefix_sum(3), 1)
        self.assertEqual(t.prefix_sum(4), 0)


class SegmentTreeTest(unittest.TestCase):

    def test_instantiation(self):
        SegmentTree([])
        SegmentTree(range(10))
        SegmentTree(range(-10, 10, 1))
        SegmentTree([1])
        SegmentTree([-1, 0, 1, 0, -1, 0, 1])

    def test_compute(self):
        t = SegmentTree(range(100))
        self.assertEqual(t.compute(0, 99), 0)
        self.assertEqual(t.compute(10, 99), 10)
        self.assertEqual(t.compute(13, 99), 13)
        self.assertEqual(t.compute(99, 99), 99)

        t = SegmentTree([-1, 1, 0, 1, -1])
        self.assertEqual(t.compute(0, 0), -1)
        self.assertEqual(t.compute(0, 2), -1)
        self.assertEqual(t.compute(1, 2), 1)
        self.assertEqual(t.compute(1, 4), 0)
        self.assertEqual(t.compute(1, 5), -1)


if __name__ == '__main__':
    unittest.main()
