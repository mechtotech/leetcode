# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        sentinel = ListNode("dummy",head)
        curr = head
        prev= sentinel
        
        while curr:
            if curr.val == val:
                prev.next= curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        
        return sentinel.next
                
            
            
        
            
        