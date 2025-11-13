class Solution(object):
    def frequencySort(self, s):
        c = {}
        for char in s:
            c[char] = c.get(char,0) + 1
        sorted_char = sorted(c.items(), key=lambda x: x[1], reverse=True)
        result = ""
        for char,v in sorted_char:
            result +=char*v
        return result 


        
       