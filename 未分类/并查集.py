class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n
        self.size = list(range(n))
        # 父结点初始指向自己
        for i in range(n):
            self.parent[i] = i
            self.size[i] = 1

    def find(self, i):
        inital_i = i
        while self.parent[i] != i:
            i = self.parent[i]
        self.parent[inital_i] = i  # 路径压缩
        return i

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if self.size[rootX] > self.size[rootY]:
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]
        else:
            self.parent[rootX] = rootY
            self.size[rootY] += self.size[rootX]
        self.count -= 1

    def count(self):
        return self.count

    def connected(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        return rootX == rootY


uf = UnionFind(100)
uf.union(1, 10)
uf.union(10, 13)
uf.union(13, 18)

print(uf.connected(1, 18))
print(uf.count)
