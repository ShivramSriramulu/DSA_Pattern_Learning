class Solution(object):
    def secondHighest(self, s):

        freq = {}  

        for ch in s:
            if ch.isdigit():                     
                freq[ch] = freq.get(ch, 0) + 1   

        if len(freq) < 2:    
            return -1

       
        sorted_num = sorted(freq.items(), key=lambda x: int(x[0]), reverse=True)

        
        return int(sorted_num[1][0])
