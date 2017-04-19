class BinaryIndexedTree(object):

    def __init__(self, values):
        super(BinaryIndexedTree, self).__init__()

        self._tree = [0] + values

        n_len = len(values)
        for idx in xrange(1, n_len):
            n_idx = idx + (idx & -idx)
            if n_idx <= n_len:
                self._tree[n_idx] += self._tree[idx]

    def prefix_sum(self, idx):
        idx += 1
        s = 0
        while idx:
            s += self._tree[idx]
            idx -= idx & -idx
        return s

    def update(self, idx, v):
        idx += 1
        delta = v - self._tree[idx]
        while idx < len(self._tree):
            self._tree[idx] += delta
            idx += idx & -idx
