class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value


N = {i: TreeNode(i) for i in range(1, 8)}

root = N[1]

N[1].left = N[2]
N[1].right = N[3]

N[2].left = N[4]
N[2].right = N[5]

N[3].right = N[6]
N[6].left = N[7]

#        1
#       / \
#      2   3
#     / \   \
#    4   5   6
#           /
#          7

# 不存在重复添加问题

import pudb
pudb.set_trace()

def bfs(T):
    Q = []
    deep = 1
    Q.append(T)
    while len(Q):
        sz = len(Q)
        for _ in range(sz):
            cur = Q.pop(0)
            if not cur.left and not cur.right:
                return deep
            if cur.left:
                Q.append(cur.left)
            if cur.right:
                Q.append(cur.right)
        deep += 1
    return deep


r = bfs(root)
print(r)
