A = [0, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 5, 6, 7, 8, 8, 8, 8]

# ready ok
s = 0
# index of next diff neum
f = 1

print(A)
for i in range(1, len(A)):
    if A[i] != A[s]:
        f = i
        break
# f 指向第一个不同于A[s] 的元素的下标

while f < len(A):
    loop_broken = False
    s += 1
    A[s] = A[f]
    for j in range(f+1, len(A)):
        if A[j] != A[s]:
            f = j
            loop_broken = True
            break
    if not loop_broken:
        break



print(A[:s+1])


