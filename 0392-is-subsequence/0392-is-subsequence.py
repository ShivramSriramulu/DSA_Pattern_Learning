class Solution(object):
    def isSubsequence(self, s, t):
        slow = 0

        for fast in range(len(t)):
            if slow < len(s) and s[slow] == t[fast]:
                slow += 1

        return slow == len(s)
