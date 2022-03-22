# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        h = head
        t = head
        
        
        while h.next and h.next.next:
            h = h.next.next
            t = t.next
        
        curr= t.next
        t.next = None
        
        prev=None
        
        while curr:
            succ = curr.next
            curr.next = prev
            prev = curr
            
            curr = succ
        
        curr = head
        curr2 = prev
        
        
        while curr and curr2:
            if curr.val != curr2.val:
                return False
            curr = curr.next
            curr2=curr2.next
        
        return True
            
      