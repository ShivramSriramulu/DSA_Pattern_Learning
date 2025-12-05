class Solution(object):
    def findMaxAverage(self, nums, k):
        w_sum = sum(nums[:k])
        max_sum = w_sum

        l = 0
        for r in range(k,len(nums)):
            w_sum +=nums[r]
            w_sum -=nums[l]
            l +=1

            max_sum = max(max_sum,w_sum)
        return float(max_sum) / k
   
        