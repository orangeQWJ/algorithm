class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val


A = {i: TreeNode(i) for i in range(1, 8)}

rootA = A[1]
A[1].left = A[2]
A[1].right = A[3]

A[2].left = A[4]
A[2].right = A[5]

A[3].right = A[6]
A[6].left = A[7]

#        1
#       / \
#      2   3
#     / \   \
#    4   5   6
#           /
#          7


# 遍历树
def travel(T):
    print(T.val)
    if T.left != None:
        travel(T.left)
    if T.right != None:
        travel(T.right)

# 处理None的时机不同
def travel2(T):
    if T == None:
        return
    print(T.val)
    travel2(T.left)
    travel2(T.right)


travel(rootA)
travel2(rootA)

