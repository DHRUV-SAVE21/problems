class Solution(object):
    def reverseList(self, head):
        prev=None 
        curr=head
        while curr:
            t=curr.next 
            curr.next=prev
            prev=curr
            curr=t
        return prev
