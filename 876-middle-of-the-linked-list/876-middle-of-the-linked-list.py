# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        h = head
        t = head
        
        while h.next and h.next.next:
            h = h.next.next
            t= t.next
            
        if h.next is not None:
            return t.next
        else:
            return t
        
        