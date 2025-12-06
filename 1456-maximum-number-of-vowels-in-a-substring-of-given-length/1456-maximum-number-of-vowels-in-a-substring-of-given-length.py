class Solution(object):
    def maxVowels(self, s, k):
        vowels = {"a", "e", "i", "o", "u"}

       
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        l = 0
        max_vowels = count
        for right in range(k, len(s)):
            if s[right] in vowels:
                count +=1
            if s[l] in vowels:
                count -=1
            l +=1
            max_vowels = max(max_vowels,count)

        return max_vowels
