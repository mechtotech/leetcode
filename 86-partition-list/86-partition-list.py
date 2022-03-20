# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        sentinels = ListNode()
        tails = sentinels
        
        sentinell = ListNode()
        taill = sentinell
        
        curr = head
        
        while curr:
            succ = curr.next
            curr.next  = None
            if curr.val < x:
                tails.next = curr
                tails =curr
            else:
                taill.next = curr
                taill =curr
            
            
            curr = succ
        
        tails.next = sentinell.next
        
        return sentinels.next