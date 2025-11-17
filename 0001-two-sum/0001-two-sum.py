class Solution(object):
    def twoSum(self, nums, target):
        hash={}
        for i,num in enumerate(nums):
            c=target - num
            if c in hash:
                return [hash[c],i]
            hash[num]=i
        