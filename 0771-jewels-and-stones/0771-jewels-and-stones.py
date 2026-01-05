class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        freq = {}
        count = 0
        for char in stones:
            freq[char] = freq.get(char,0) + 1
        for char in jewels:
            count+=freq.get(char,0)
        return count
       
       