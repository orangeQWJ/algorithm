class Solution:
    def trap1(self, height):
        water_sum = 0
        for i, v in enumerate(height):
            if height[:i]:
                l_max = max(height[:i])
            else:
                l_max = 0
            if height[i+1:]:
                r_max = max(height[i+1:])
            else:
                r_max = 0
            print(l_max, r_max, min(l_max, r_max))
            if v <= min(l_max, r_max):
                water_sum += min(l_max, r_max) - v
            else:
                water_sum += 0
        return water_sum

    def trap2(self, height):
        water_sum = 0
        L_max = [max(height[:i]) if height[:i]
                 else 0 for i in range(len(height))]
        R_max = [max(height[i+1:]) if height[i+1:]
                 else 0 for i in range(len(height))]
        for i, v in enumerate(height):
            l_max = L_max[i]
            r_max = R_max[i]
            if v <= min(l_max, r_max):
                water_sum += min(l_max, r_max) - v
            else:
                water_sum += 0
        return water_sum

    def trap(self, height):
        water_sum = 0
        L_max = [0] * len(height)
        for i in range(1, len(height)):
            L_max[i] = max(L_max[i-1], height[i-1])

        R_max = [0] * len(height)
        for i in range(len(height)-2, -1, -1):
            R_max[i] = max(R_max[i+1], height[i+1])
        for i, v in enumerate(height):
            l_max = L_max[i]
            r_max = R_max[i]
            if v <= min(l_max, r_max):
                water_sum += min(l_max, r_max) - v
            else:
                water_sum += 0

        return water_sum


s = Solution()

r = s.trap([0, 7, 1, 9,  4, 6])
