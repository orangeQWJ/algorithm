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

#        1                   #             50
#       / \                  #            /  \
#      2   3                 #           40   60
#     / \   \                #          / \    \
#    4   5   6               #         20 45   68
#           /                #                 /
#          7                 #                67

A[1].val = 50
A[2].val = 40
A[3].val = 60
A[4].val = 20
A[5].val = 45
A[6].val = 68
A[7].val = 67


def isInTree(T, target):
    if T == None:
        return False
    if T.val == target:
        return True
    return isInTree(T.left, target) or isInTree(T.right, target)


def isInBST(T, target):
    if T == None:
        return False
    if T.val == target:
        return True
    elif target > T.val:
        return isInBST(T.right, target)
    elif target < T.val:
        return isInBST(T.left, target)

print(isInTree(rootA, 69))
print(isInTree(rootA, 67))
print(isInBST(rootA, 69))
print(isInBST(rootA, 67))
