# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        sentinel = ListNode("dummy",head)
        tail =sentinel
        curr  = head
        length = 0
        while curr:
            length +=1
            tail= curr
            curr = curr.next
        
        r = length - (k%length)
        if length == r:
            return head
        curr= head
        prev= sentinel
        index = 0
        while curr and index != r:
            index+=1
            prev= curr
            curr = curr.next
        prev.next = None
        tail.next = sentinel.next
        sentinel.next = curr
        
        
        return sentinel.next
    
        