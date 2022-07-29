# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None
        
        
        sentinelo = ListNode("dummy")
        tailo = sentinelo
        
        sentinele = ListNode("dummy")
        taile = sentinele
        
        
        index = 1
        curr = head
        prev = None
        
        while curr:
            succ= curr.next
            if index%2 !=0:
                tailo.next = curr
                tailo = curr
                tailo.next = None
                curr = succ
                
            else:
                taile.next = curr
                taile = curr
                taile.next = None
                curr = succ
            index+=1
        
        sentinel = ListNode("dummy")
        tail = sentinel
                
        curr2 = sentinelo.next
        curr1 = sentinele.next
        
        while curr1 and curr2:
            succ1 = curr1.next
            tail.next = curr1 #s--->2
            tail = curr1
            curr1 = succ1
            
            succ2 = curr2.next
            tail.next = curr2 #s--->2-->1
            tail = curr2
            curr2= succ2
            
        
        while curr2:      #s--->2--->1--->3
                           #    new_head ==>2
            tail.next = curr2
            tail = curr2
            curr2 = curr2.next
        return sentinel.next
            
            
            
            
            
            
            
            
            
            
            
        
    
                
                
                
        
        
        