# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None
        
        
        #sentinel = ListNode("dummy",head)
        
        prev = head
        curr = head.next
        step = 0
        while curr:
            if step%2 == 0:
                currvalue = curr.val
                prevvalue = prev.val
                curr.val = prevvalue
                prev.val = currvalue
                
            step+=1
            prev = curr
            curr= curr.next
            
        
        return head
                
            
            
        
        