class Solution(object):
    def isPowerOfTwo(self, n):
        if n<=0:
            return False

        while n % 2==0:
            n //=2
        
        return n==1
    
# if n<=0:
#     return False

# x=1
# while x<n:
#     x *=2

# return x==n