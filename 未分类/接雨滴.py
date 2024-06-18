def r_h_i(index, A):
    for i in range(index+1, len(A)):
        if A[i] >= A[index]:
            return i
    return -1

def main():
    hight = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(hight)
    init = sum(hight)
    i = 0
    while i < len(hight):
        index = r_h_i(i, hight)
        if index != -1:
            for j in range(i, index):
                hight[j] = hight[i]
            i = index
        else:
            i += 1
    fin = sum(hight)
    print(fin-init)
    print(hight)

main()
