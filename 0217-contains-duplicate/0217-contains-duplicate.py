class Solution(object):
    def containsDuplicate(self, nums):
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for k,v in freq.items():
            if v >= 2:
                return True
        return False
   