# 1290. Convert Binary Number in a Linked List to Integer
class Solution(object):
    def getDecimalValue(self, head):
       nums=0
       curr=head

       while curr:
        nums=nums*2+curr.val
        curr=curr.next

       return nums
