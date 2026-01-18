class Solution(object):
    def intersection(self, nums1, nums2):
        result = []
        for num in nums2:
            if num in nums1 and num not in result:
                result.append(num)
        return result

       