class Solution(object):
    def findTheDifference(self, s, t):
        xor_value=0
        for ch in s:
            xor_value ^=ord(ch)
        for ch in t :
            xor_value ^=ord(ch)

        return chr(xor_value) 
        