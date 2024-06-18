class Solution:
    def moveZeroes(self, nums):
        """
        i: 当前可入住房间指引
        j: 需要入住的顾客
        i: 初始化为第一个0的下标
        j: i 之后 第一个!0的下标

        结束条件:
            1. 一开始就没有0
            2. 找不到入住的客人了

        """
        i = j = 0
        flag1 = False # nums数组中有没有0
        for index, value in enumerate(nums):
            if value == 0:
                flag1 = True
                i = index
                flag2 = False
                for x in range(i+1, len(nums)):
                    if nums[x] != 0:
                        j = x
                        flag2 = True
                        break
                if flag2 == False:
                    return
                break
        if flag1 == False: # 如果没有0,直接退出
            return
            

        print(i, j)
        while j < len(nums):
            nums[i] = nums[j]
            i += 1
            flag3 = False
            for index in range(j+1, len(nums)):
                if nums[index]!=0:
                    flag3 = True
                    j = index
                    break
            if flag3 == False:
                for index in range(i, len(nums)):
                    nums[index] = 0
                break
        print(nums)

s = Solution()
s.moveZeroes([0,1,0,3,12])
s.moveZeroes([1,0])

