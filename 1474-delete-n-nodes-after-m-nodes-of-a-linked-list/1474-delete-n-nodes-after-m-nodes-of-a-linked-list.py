# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        
        sentinel = ListNode("dummy",head)
        prev= sentinel
        curr = head
        
        while curr:
            steps = 0 
            while curr and steps < m:
                steps+=1
                prev = curr
                curr=curr.next
            
            if curr is None:
                return head
            
            p = curr
            while p and steps < m+n:
                p= p.next
                steps+=1
            
            prev.next = p
            curr = p
        
        return sentinel.next
                
"""
_ _ _ _ _ _ _

"""
        
        