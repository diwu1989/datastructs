class SegmentTree(object):

    def __init__(self, values, op=min):
        super(SegmentTree, self).__init__()

        self._n = len(values)
        self._tree = ([0] * self._n) + values
        self._op = op

        for idx in xrange(self._n - 1, 0, -1):
            self._tree[idx] = op(self._tree[idx * 2],
                                 self._tree[idx * 2 + 1])

    def update(self, idx, v):
        idx += self._n
        self._tree[idx] = v

        while idx > 1:
            idx /= 2
            self._tree[idx] = self._op(self._tree[idx * 2],
                                       self._tree[idx * 2 + 1])

    def compute(self, left, right):
        left += self._n
        right += self._n

        v = self._tree[left]
        while left < right:
            if left & 1:
                v = self._op(v, self._tree[left])
                left += 1
            if right & 1:
                right -= 1
                v = self._op(v, self._tree[right])
            left /= 2
            right /= 2
        return v
