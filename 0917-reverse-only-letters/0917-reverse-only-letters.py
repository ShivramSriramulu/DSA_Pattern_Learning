class Solution(object):
    def reverseOnlyLetters(self, s):
        s = list(s)
        letters = []
        for fast in range(len(s)):
            if s[fast].isalpha():
                letters.append(s[fast])
        letters.reverse()
        slow = 0
        for i in range(len(s)):
            if s[i].isalpha():
                s[i] = letters[slow]
                slow +=1
                
        return "".join(s)



     