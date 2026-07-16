# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head: Optional[ListNode])->Optional[ListNode]:
        if not head:
            return None
        l = head
        r = head.next
        while l and r:
            temp = r.next
            r.next = l
            l = r
            r = temp
        head.next = None
        return l
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        rhead = self.reverse(head)
        if n==1: 
            rhead = rhead.next
        else:
            l = None
            r = rhead
            for i in range(0,n-1):
                l = r
                r = r.next
            l.next = r.next
        return self.reverse(rhead)
        