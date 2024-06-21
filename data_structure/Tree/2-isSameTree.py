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


# 两棵树是否相等
B = {i: TreeNode(i) for i in range(1, 8)}

rootB = B[1]
B[1].left = B[2]
B[1].right = B[3]

B[2].left = B[4]
B[2].right = B[5]

B[3].right = B[6]
B[6].left = B[7]
B[7].val = 777

#        1                   #        1
#       / \                  #       / \
#      2   3                 #      2   3
#     / \   \                #     / \   \
#    4   5   6               #    4   5   6
#           /                #           /
#          7                 #          777


def isSameTree(T1, T2):
    if T1.val != T2.val:
        return False
    leftSame = False
    rightSame = False

    if T1.left != None and T2.left != None:
        leftSame = isSameTree(T1.left, T2.left)
    elif T1.left == None and T2.left == None:
        leftSame = True
    else:
        return False

    if T1.right != None and T2.right != None:
        rightSame = isSameTree(T1.right,  T2.right)
    elif T1.right == None and T2.right == None:
        rightSame = True
    else:
        return False

    return leftSame and rightSame


def isSameTree2(T1, T2):
    if T1 == None and T2 == None:
        return True
    if T1 == None or T2 == None:
        return False
    if T1.val != T2.val:
        return False
    return isSameTree2(T1.left, T2.left) and isSameTree2(T1.right, T2.right)


print(isSameTree(rootA, rootB))
print(isSameTree2(rootA, rootB))
B[7].val = 7
print(isSameTree(rootA, rootB))
print(isSameTree2(rootA, rootB))
