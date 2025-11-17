class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        mapst = {}
        mapts = {}
        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]

            if c1 in mapst and mapst[c1] != c2:
                return False
            if c2 in mapts and mapts[c2] != c1:
                return False
            mapst[c1] = c2
            mapts[c2] = c1
        return True


       