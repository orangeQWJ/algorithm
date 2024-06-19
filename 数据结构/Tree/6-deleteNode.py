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


def deleteNode(T, target):
    if T == None:
        return None
    if T.val == target:
        if T.left == None and T.right == None: # 无子节点
            return None
        if T.left != None and T.right == None: # 一个子节点
            return T.left
        if T.right != None and T.left == None: 
            return T.right
        minNode = geMin(T.right)
        deleteNode(T, minNode.val)
        T.val = minNode.val
    elif target < T.val:
        T.left = deleteNode(T.left, target)
    elif target > T.val:
        T.right = deleteNode(T.right, target)
    return T

def geMin(T):
    while T.left != None:
        T = T.left
    return T
    
def travel(T):
    if T == None:
        return
    travel(T.left)
    print(T.val)
    travel(T.right)

travel(rootA)
print("////////")

print("del:50")
deleteNode(rootA, 50)
travel(rootA)
print("////////")

print("del:45")
deleteNode(rootA, 45)
travel(rootA)
print("////////")

print("del:68")
deleteNode(rootA, 68)
travel(rootA)
print("////////")
