# 190. Reverse Bits
class Solution(object):
    def reverseBits(self, n):
        res=0
        for _ in range(32):
            res=(res<<1) | (n & 1)
            n>>=1
        return res
