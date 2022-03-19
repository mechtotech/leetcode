# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        sentinel = ListNode()
        
        curr = head
        
        while curr:
            succ = curr.next
            curr.next = None
            
            
            prev = sentinel
            curr2 =sentinel.next
            
            while curr2 and curr.val > curr2.val:
                prev= curr2
                curr2 = curr2.next
            
            prev.next = curr
            curr.next = curr2
            
            
            curr = succ
        
        return sentinel.next
            