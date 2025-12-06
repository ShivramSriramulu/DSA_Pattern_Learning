class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        
        window_sum = sum(arr[:k])
        count = 0
        if window_sum/k >=threshold:
            count += 1 
  
        l = 0
        for r in range(k,len(arr)):
            window_sum += arr[r]
            window_sum -= arr[l]
            l += 1
            if window_sum/k >= threshold:
                count +=1
        return count

        




     