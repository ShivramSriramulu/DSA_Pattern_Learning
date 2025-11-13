class Solution(object):
    def majorityElement(self, nums):
        c = {}
        n = len(nums)
        for num in nums:
            c[num] = c.get(num,0) + 1
        
        for k,v in c.items():
            if v > n/2:
                return k
       