class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        x=0
        for i in range(n+1):
            x ^= i
        for v in nums:
            x ^= v
        return x
        