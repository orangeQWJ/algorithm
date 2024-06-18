import random

nums = [random.randint(1, 5) for _ in range(20)]
# preSum[i] = sum[:i+1]
preSum = [sum(nums[:i+1]) for i in range(len(nums))]

k = 9

def sum(i,j):
    # [i,j] both the end
    return preSum[j] - preSum[i-1]

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if sum(i,j) == k:
            print(nums[i:j+1])

