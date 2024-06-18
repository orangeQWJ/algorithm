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


def visual():
    for x in A:
        for j in x:
            print(j, end=" ")
        print()
    print()


A = [
    list("xxxxo"),
    list("xxxox"),
    list("ooxox"),
    list("xoxxx"),
]

M = 4
N = 5

uf = UnionFind(M*N+1)
OKK = M*N

for j in range(N):
    if A[0][j] == "o":
        uf.union(OKK, 0*M+j)
    if A[M-1][j] == "o":
        uf.union(OKK, (M-1)*M+j)

for i in range(M):
    if A[i][0] == "o":
        uf.union(OKK, i*M + 0)
    if A[i][N-1] == "o":
        uf.union(OKK, i*M + N-1)

visual()
d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
for i in range(1, M-1):
    for j in range(1, N-1):
        if A[i][j] == 'o':
            for k in range(4):
                index_i = i + d[k][0]
                index_j = j + d[k][1]
                if A[index_i][index_j] == 'o':
                    uf.union(i*M+j, index_i*M + index_j)


for i in range(M):
    for j in range(N):
        if A[i][j] == 'o' and (not uf.connected(OKK, i*M+j)):
            A[i][j] = 'x'

visual()
