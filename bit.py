class BinaryIndexedTree(object):

    def __init__(self, values):
        super(BinaryIndexedTree, self).__init__()

        self.__tree = [0] + values

        n_len = len(values)
        for i in xrange(1, n_len):
            n_idx = i + self.__least_bit(i)
            if n_idx <= n_len:
                self.__tree[n_idx] += self.__tree[i]

    def prefix_sum(self, idx):
        idx += 1
        s = 0
        while idx:
            s += self.__tree[idx]
            idx -= self.__least_bit(idx)
        return s

    def update(self, idx, v):
        idx += 1
        delta = v - self.__tree[idx]
        while idx < len(self.__tree):
            self.__tree[idx] += delta
            idx += self.__least_bit(idx)

    def __least_bit(self, idx):
        return idx & -idx
