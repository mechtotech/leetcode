# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        sentinel = ListNode("dummy",head)
        prev = sentinel
        curr = head
        
        
        while curr:
            
            if curr.next and curr.val==curr.next.val:
                p= curr.next
                while p and p.val == curr.val:
                    p=p.next
                
                prev.next = p
                curr = p
                
            
            
            else:
                prev= curr
                curr = curr.next
        
        return sentinel.next
        