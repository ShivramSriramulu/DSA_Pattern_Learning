class Solution(object):
    def twoSum(self, nums, target):
        map ={}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in map:
                return [map[comp],i]
            map[num] = i
      