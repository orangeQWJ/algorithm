class Solution:
    def findAnagrams(self, s: str, p:str):
        '''
        from collections import defaultdict
        need = defaultdict(int)
        for x in p:
            need[x] += 1
        '''
        need = {}
        for key in p:
            if key not in need:
                need[key] = 1
            else:
                need[key] += 1

        window = {}
        for key in p:
            window[key] = 0

        L = R = 0
        valid_num = 0
        res = []

        while R < len(s):
            c = s[R]
            R += 1
            if c in window:
                window[c] += 1
                if window[c] == need[c]:
                    valid_num += 1
            while valid_num == len(need):
                if R-L == len(p):
                    res.append(L)
                d = s[L]
                L += 1
                if d in window:
                    if window[d] == need[d]:
                        valid_num -= 1
                    window[d] -= 1
        return res

s = Solution()

r = s.findAnagrams('cbaebabacd', 'abc')
print(r)
