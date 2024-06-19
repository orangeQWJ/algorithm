# 判断两棵树是否相同

1. `isSameTree2` 吸取之前的经验,允许遍历空子树

## 重要经验

```python
# 两个None
if T1 == None and T2 == None:
	return True
# 仅有一个None
if T1 == None or T2 == None:
	return False
# 没有None
if T1.val != T2.val :
	return False

```

