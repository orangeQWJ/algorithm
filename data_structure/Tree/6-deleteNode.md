# 在 BST 中删除一个数

## 框架

```python
def deleteNode(T, target):
    if T == None:
        return None
    if T.val == target:
        pass
        #开始删除
    elif target < T.val:
        T.left = deleteNode(T.left, target)
    elif target > T.val:
        T.right = deleteNode(T.right, target)
    return T
```

## 当前节点(67)没有孩子

```python
             50
            /  \
           40   60
          / \    \
         20 45   68
                 /
                67 <-

    if T.val == target:
        if T.left == None and T.right == None:
            return None
```

## 当前节点只有左孩子

```python
             50
            /  \
           40   60
          / \    \
         20 45   68 <-
                 /
                67
	if T.left != None and T.right == None:
		return T.left
```

## 当前节点有右孩子

```python
             50
            /  \
           40   60 <-
          / \    \
         20 45   68
                 /
                67
	if T.right != None and T.left == None:
		return T.right
```

## 当前节点有两个孩子

```python
         ->  50
            /  \
           40   60
          / \    \
         20 45   68
                 /
                67
```

### BST 的性质对节点 50 有两个要求

1. 小于 右子树的所有节点 => 小于 右子树的最小节点 `60`
2. 大于 左子树的所有节点 => 大于 左子树的最大节点 `45`

### 如何寻找子树的最小/最大节点

```python
def getMin(T):
    while T.left != None:
        T = T.left
    return T
 def getMax(T):
	while T.right != None:
		T = T.right
	return T
```

### 右子树的最小节点 60 替换 50 的位置

1. 小于 右子树(删除 60 节点后)的所有节点 => 小于 右子树的最小节点 `60` -> `67`
2. 大于 左子树的所有节点 => 大于 左子树的最大节点 `45`

### 删除拥有双孩子步骤

1. 找到右子树中的最小值,删除 `60` 节点
   - 💡 最小值一定没有左节点,最大值一定没有右节点
   - 对于有一个孩子的情况,我们已经解决了
2. 将 `50` 节点的值替换为 `60`

```python
        minNode = geMin(T.right)
        deleteNode(T, minNode.val)
        T.val = minNode.val

```
