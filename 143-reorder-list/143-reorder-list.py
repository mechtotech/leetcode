# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        h = head
        t = head
        
        while h.next and h.next.next:
            h = h.next.next
            t= t.next
        
        curr= t.next
        t.next = None
        
        prev = None
        while curr:
            succ = curr.next
            curr.next = prev
            prev= curr
            curr = succ
        sentinel = ListNode()
        tail  = sentinel
        while head and prev:
            tail.next = head
            tail = head
            head = head.next
            tail.next = prev
            tail = prev
            prev = prev.next
        while head:
            tail.next = head
            tail = head
            head = head.next
        while prev:
            tail.next = prev
            tail = prev
            prev = prev.next
        
        
        
        return sentinel.next
            
                