class Solution(object):
    def removeDuplicates(self, s):
        arr =list(s)
        slow = 0

        for fast in range(len(arr)):
            if slow > 0 and arr[fast] == arr[slow-1]:
                slow -=1
            else:
                arr[slow] = arr[fast]
                slow +=1
        return "".join(arr[:slow])



       