class UnionFind:
    def __init__(self, capacity):
        self.parent = list(range(capacity))

    def find_ancester(self, x):
        p = x
        while p != self.parent[p]:
            p = self.parent[p]
        self.parent[x] = p  # 认祖先为父,加快后续搜索速度
        return p

    def union(self, p, q):
        p_ancester = self.find_ancester(p)
        q_ancester = self.find_ancester(q)
        self.parent[q_ancester] = p_ancester

    def connected(self, p, q):
        p_ancester = self.find_ancester(p)
        q_ancester = self.find_ancester(q)
        return p_ancester == q_ancester

    def count(self):
        sum = 0
        for i, x in enumerate(self.parent):
            if i == x:
                sum += 1
        return sum
if __name__ == "__main__":
    uf = UnionFind(100)
    uf.union(1, 10)
    uf.union(10, 99)
    uf.union(12, 99)
    uf.union(2, 12)
    print(uf.connected(1, 2))
