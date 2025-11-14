class Solution(object):
    def kthDistinct(self, arr, k):
        freq ={}
        for char in arr:
            freq[char] = freq.get(char,0) + 1
        count = 0
        for char in arr:
            if freq[char] == 1:
                count +=1
            if count == k:
                return char
        return ""


       