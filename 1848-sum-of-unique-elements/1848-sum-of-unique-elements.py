class Solution(object):
    def sumOfUnique(self, nums):
        c ={}
        for num in nums:
            c[num] = c.get(num,0) + 1
        total = 0
        for k,v in c.items():
            if v == 1:
                total += k
        return total
        