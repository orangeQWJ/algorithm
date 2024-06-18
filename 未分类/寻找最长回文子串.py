s = "aasdfkhabcdffdcbaskdfjao9i8jskdjf"
s = list(s)

def rHw(s, i, j):
    if i <0 or j >= len(s):
        return []
    while i >= 0 and j < len(s):
        if s[i] == s[j]:
            i -= 1
            j += 1
        else:
            return s[i+1:j]
    return s[i+1:j]


def main(s):
    max_length_hw = s[0]
    for i in range(0, len(s)):
        s1 = rHw(s, i, i)
        s2 = rHw(s, i, i+1)
        s_m = s1 if len(s1) > len(s2) else s2
        max_length_hw = max_length_hw if len(max_length_hw) > len(s_m) else s_m
    print(max_length_hw)
main(s)
