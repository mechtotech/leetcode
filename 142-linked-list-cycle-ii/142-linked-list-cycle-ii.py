# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        if head is None:
            return None
        
        h = head
        t = head
        
        while h.next and h.next.next:
            
            h = h.next.next
            t= t.next
            
            if h == t:
                third = head
                while third != t:
                    third= third.next
                    t = t.next
                return third
                    
                
        
        return None