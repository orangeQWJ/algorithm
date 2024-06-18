class Solution:
    def lengthOfLongestSubstring(self, s):
        R = L = 0
        window = {}
        for x in s:
            window[x] = 0

        max_length = 0
        print(window)
        while R < len(s):
            c = s[R]
            R += 1
            window[c] += 1
            if window[c] <= 1:
                max_length = max(R - L, max_length)
            while window[c] > 1:
                max_length = max(R - L - 1, max_length)
                d = s[L]
                L += 1
                window[d] -= 1
        return max_length
s = Solution()
r = s.lengthOfLongestSubstring(" ")
print(r)
