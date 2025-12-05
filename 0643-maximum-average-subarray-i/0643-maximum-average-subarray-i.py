class Solution(object):
    def findMaxAverage(self, nums, k):
        # Step 1: compute the sum of the first window
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # Step 2: slide the window across the array
        left = 0
        for right in range(k, len(nums)):
            window_sum += nums[right]      # add the new element
            window_sum -= nums[left]       # remove the outgoing element
            left += 1                      # move the window forward

            max_sum = max(max_sum, window_sum)

        # Step 3: return the maximum average
        return float(max_sum) / k
