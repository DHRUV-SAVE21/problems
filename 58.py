class Solution(object):
    def lengthOfLastWord(self, s):
        s=s.rstrip()
        count=0
        for ch in reversed(s):
            if ch==' ':
               break
            count+=1
            
        return count 
