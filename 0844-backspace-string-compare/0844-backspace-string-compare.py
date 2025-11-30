class Solution(object):
    def backspaceCompare(self, s, t):
        
        def build(string):
            arr = list(string)
            slow = 0   

            for fast in range(len(arr)):
                if arr[fast] != "#":
                    arr[slow] = arr[fast]
                    slow += 1
                else:
                    if slow > 0:
                        slow -= 1  
            
            return "".join(arr[:slow])

        return build(s) == build(t)
