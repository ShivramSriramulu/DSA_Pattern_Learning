class Solution(object):
    def uniqueOccurrences(self, arr):
        freq = {}
        for num in arr:
            freq[num] = freq.get(num,0) + 1
        freq_values = freq.values()
        return len(freq_values) == len(set(freq_values))
        
       