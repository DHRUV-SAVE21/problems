class Solution:
    def longestSubarray(self, nums):
        max_elem = max(nums) 

        curr_len = 0
        max_len = 0

        for num in nums:
            if num == max_elem:
                curr_len += 1
                max_len = max(max_len, curr_len)
            else:
                curr_len = 0

        return max_len
