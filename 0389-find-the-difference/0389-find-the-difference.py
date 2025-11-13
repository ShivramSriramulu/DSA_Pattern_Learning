class Solution(object):
    def findTheDifference(self, s, t):
        count_s = {}
        count_t = {}

        for char in s:
            count_s[char] = count_s.get(char, 0) + 1


        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        for k, v in count_t.items():
            if count_s.get(k, 0) != v:
                return k

        
        