class Solution:
    def maxArea(self, height):
        max_A = 0
        for i, h1 in enumerate(height):
            for j in range(i+1, len(height)):
                h2 = height[j]
                h_min = min(h1, h2)
                length = j-i
                max_A = max(max_A, length * h_min)
        return max_A

    def maxArea2(self, height):
        i = 0
        j = len(height) - 1
        max_A = 0
        while i < j:
            min_h = min(height[j], height[i])
            length = j - i
            max_A = max(max_A, min_h*length)
            if height[j] > height[i]:
                i += 1
            else:
                j -= 1
        return max_A


s = Solution()
r = s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(r)
r = s.maxArea2([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(r)
