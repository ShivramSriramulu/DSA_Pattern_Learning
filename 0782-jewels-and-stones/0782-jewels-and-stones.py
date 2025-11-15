class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        j ={}

        for char in jewels:
            j[char] = j.get(char,0) + 1
        count = 0

        for char in stones:
            if char in j:
                count += 1
        return count 


        