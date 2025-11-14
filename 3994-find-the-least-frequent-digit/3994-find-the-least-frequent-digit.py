class Solution(object):
    def getLeastFrequentDigit(self, n):
        freq = {}
        for digit in str(n):
            freq[digit] = freq.get(digit, 0) + 1
        sorted_digits = sorted(freq.items(), key=lambda x: (x[1], int(x[0])))
        return int(sorted_digits[0][0])
