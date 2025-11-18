class Solution(object):
    def secondHighest(self, s):
        digit = set()

        for ch in s:
            if ch.isdigit():
                digit.add(int(ch))
        
        if len(digit) <2:
            return -1
        
        sorted_digit = sorted(digit, reverse = True)
        return sorted_digit[1]

     