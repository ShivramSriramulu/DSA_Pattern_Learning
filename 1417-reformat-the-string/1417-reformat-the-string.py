class Solution(object):
    def reformat(self, s):
        letters = []
        digits = []


        for ch in s:
            if ch.isalpha():
                letters.append(ch)
            else:
                digits.append(ch)

        
        if abs(len(letters) - len(digits)) > 1:
            return ""

        
        if len(letters) >= len(digits):
            first, second = letters, digits
        else:
            first, second = digits, letters

        i = j = 0
        turn = 0  
        result = []

 
        while i < len(first) or j < len(second):

            if turn == 0 and i < len(first):
                result.append(first[i])
                i += 1
            elif turn == 1 and j < len(second):
                result.append(second[j])
                j += 1

            turn ^= 1  

        return "".join(result)
