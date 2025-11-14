class Solution(object):
    def frequencySort(self, s):
        count = {}
        result =""
        for char in s:
            count[char] = count.get(char,0) + 1
        sorted_str=sorted(count.items(), key = lambda x: x[1],reverse =True)
        

        for char,v in sorted_str:
            result += char * v
        return result
        
       


        
       