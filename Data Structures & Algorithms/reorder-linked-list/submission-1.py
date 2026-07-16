# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next 
        
        temp = slow.next
        slow.next = None

        # putting second half into stack
        s = []
        while temp:
            s.append(temp)
            temp = temp.next

        # stitching everything back
        left = head
        while s:
            mid = s.pop()
            right = left.next
            left.next = mid
            mid.next = right
            left = right
            