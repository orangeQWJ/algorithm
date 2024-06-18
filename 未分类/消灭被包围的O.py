A = [
        list("xxxxo"),
        list("xxxox"),
        list("ooxox"),
        list("xoxxx"),
        ]

M = 4
N = 5

def visual():
    for x in A:
        for j in x:
            print(j, end=" ")
        print()
    print()
visual()

def dfs(i, j):
    # 越界直接返回
    if i < 0 or i >= M or j < 0 or j >= N:
        return 
    if A[i][j] == "o":
        A[i][j] = "#"
        dfs(i,j+1)
        dfs(i,j-1)
        dfs(i+1,j)
        dfs(i-1,j)

# 除了和边缘相连的,其他的都会被消灭
for j in range(N):
    dfs(0, j)
    dfs(M-1, j)

for i in range(M):
    dfs(i, 0)
    dfs(i,N-1)

visual()

# 将剩下的o替换成x, 然后将# 替换成o
for i in range(M):
    for j in range(N):
        if A[i][j] == "o":
            A[i][j] = 'x'
        elif A[i][j] == '#':
            A[i][j] = "o" 

visual()
