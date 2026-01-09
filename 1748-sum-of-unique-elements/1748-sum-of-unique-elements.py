class Solution(object):
    def sumOfUnique(self, nums):
        freq = {}
        count = 0
        
        for num in nums:
            freq[num] = freq.get(num,0) + 1

        for k,v in freq.items():
            if v == 1:
                count += k
        return count




      