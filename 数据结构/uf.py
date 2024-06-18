class UnionFind():
    def __init__(self, n):
        self.count = n
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        init_x = x
        while self.parent[x] != x:
            x = self.parent[x]
        self.parent[init_x] = x
        return x

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if self.size[rootX] > self.size[rootY]:
            self.size[rootX] += self.size[rootY]
            self.parent[rootY] = rootX
        else:
            self.size[rootY] += self.size[rootX]
            self.parent[rootX] = rootY
        self.count -= 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def count(self):
        return self.count


if __name__ == "__main__":
    uf = UnionFind(100)
    uf.union(1, 10)
    uf.union(10, 99)
    print(uf.connected(1, 99))
