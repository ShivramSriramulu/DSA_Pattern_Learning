class Solution(object):
    def findTheDifference(self, s, t):
        freq = {}
        for char in s:
            freq[char] = freq.get(char,0) + 1
        for char in t:
            if freq.get(char,0) ==0:
                return char
            freq[char]-=1
       
       