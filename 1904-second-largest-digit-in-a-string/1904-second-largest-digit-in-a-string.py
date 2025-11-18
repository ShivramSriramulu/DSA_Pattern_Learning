class Solution(object):
    def secondHighest(self, s):

        freq = {}  # count frequency of only digits

        for ch in s:
            if ch.isdigit():                     # only numeric
                freq[ch] = freq.get(ch, 0) + 1   # count frequency

        if len(freq) < 2:    # not enough unique digits
            return -1

        # Sort by numeric value DESC (ignore frequency)
        sorted_num = sorted(freq.items(), key=lambda x: int(x[0]), reverse=True)

        # Return the digit (key) of the second largest
        return int(sorted_num[1][0])
