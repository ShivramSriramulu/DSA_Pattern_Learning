class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        res = [0] * n

        l, r = 0, n - 1
        idx = n - 1  

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[idx] = nums[l] * nums[l]
                l += 1
            else:
                res[idx] = nums[r] * nums[r]
                r -= 1
            idx -= 1
        
        return res
