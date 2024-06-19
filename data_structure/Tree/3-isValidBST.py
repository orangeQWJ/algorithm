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


def isValidBST(T):
    leftValid = False
    if T.left == None:
        leftValid = True
    else:
        leftValid = T.val > T.left.val and isValidBST(T.left)

    rightValid = False
    if T.right == None:
        rightValid = True
    else:
        rightValid = T.val < T.right.val and isValidBST(T.right)
    return leftValid and rightValid


#        1
#       / \
#      2   3
#     / \   \
#    4   5   6
#           /
#          7
print(isValidBST(rootA))

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
print(isValidBST(rootA))

A[7].val = 69
#        50
#       /  \
#      40   60
#     / \    \
#    20 45   68
#            /
#           69
print(isValidBST(rootA))


# ❌ ❌ ❌ ❌
A[7].val = 3
#        50
#       /  \
#      40   60
#     / \    \
#    20 45   68
#            /
#           3
print(isValidBST(rootA))


def isValidBST2(T, min_val, max_val):
    # min_val < T.val < max_val
    # T.val > min_val
    # T.val < max_val
    if T == None:
        return True
    if min_val != None and T.val <= min_val:
        return False
    if max_val != None and T.val >= max_val:
        return False

    return isValidBST2(T.left, min_val, T.val) and isValidBST2(T.right, T.val, max_val)


print(isValidBST2(rootA, None, None))


