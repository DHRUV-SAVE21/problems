class Solution(object):
    def moveZeroes(self, nums):
        last=0

        for i in range(len(nums)):
            if nums[i]!=0:
                nums[last],nums[i]=nums[i],nums[last]
                last +=1
        