# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        sentinel = ListNode("dummy",head)
        curr = head
        prev = sentinel
        i = 1
        while curr and i < left:
            prev = curr
            curr = curr.next
            i+=1
            
        left_tail = prev
        prev.next = None
        middle_tail = curr
        
        
        prev =None
        while curr and i< right+1:
            succ = curr.next
            curr.next = prev
            prev= curr
            curr = succ
            i+=1
        
        middle_head = prev
        right_head = curr
        
        left_tail.next = middle_head
        middle_tail.next = right_head
        
        return sentinel.next
        
            