# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        sentinel = ListNode("dummy",head)
        
        leader = sentinel
        
        for _ in range(n):
            leader = leader.next
        
        follower  =sentinel
        prev = sentinel
        
        while leader:
            
            
            leader = leader.next
            prev= follower
            follower = follower.next
        
        prev.next = follower.next
        
        return sentinel.next
            
        
       
            
            
        
        
        