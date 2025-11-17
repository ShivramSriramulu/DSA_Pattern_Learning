class Solution(object):
    def findRepeatedDnaSequences(self, s):
        freq = {}
        for i in range(len(s)-9):
            sub=s[i:i+10]
            freq[sub] = freq.get(sub,0) + 1
        
        result =[]
        for k,v in freq.items():
            if v>1:
                result.append(k)
        return result
      
       

        