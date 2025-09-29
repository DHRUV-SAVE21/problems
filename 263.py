#Ugly Number 
class Solution(object):
    def isUgly(self, n):
        if n<=0:
            return False

        for i in [2,3,5]:
            while n%i==0:
                n//=i
        return n==1

#also check with multiple loop of while i%2==0vice versa and last check of n==1 then written the element 

        