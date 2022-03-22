# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        h = head
        t= head
        
        while h.next and h.next.next:
            h = h.next.next
            t= t.next
            
        new_head = t.next
        t.next = None
        
        prev = None
        curr = new_head
        
        while curr:
            succ = curr.next
            curr.next = prev
            prev= curr
            curr =succ
        new_head = prev
        while head and new_head:
            if head.val != new_head.val:
                return False
            head= head.next
            new_head = new_head.next
            
        
        return True
            
            
            
       
      