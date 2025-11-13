class Solution(object):
    def topKFrequent(self, nums, k):
        c ={}
        for num in nums:
            c[num] = c.get(num,0) + 1
        sorted_num = sorted(c.items(),key = lambda x:x[1], reverse =True)
        result = []
        for i in range(k):
            result.append(sorted_num[i][0])
        return result
            


        
       