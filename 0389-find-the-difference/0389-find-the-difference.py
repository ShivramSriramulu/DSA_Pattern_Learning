class Solution(object):
    def findTheDifference(self, s, t):
        c_s = {}
        for char in s:
            c_s[char] = c_s.get(char, 0) + 1

        c_t = {}
        for char in t:
            c_t[char] = c_t.get(char, 0) + 1

        for k, v in c_t.items():
            if k not in c_s or c_t[k] != c_s.get(k, 0):
                return k
