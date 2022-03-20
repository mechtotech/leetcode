# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        
        sentinels = ListNode()
        sentinell = ListNode()
        tails= sentinels
        taill=sentinell
        
        # pluck the node from original linked list
        # add =>x to taill node and rest to tails
        # tails.next = sentinell.next
        #increment the curr on orginal 
        #return sentinels.next 
        
        curr  = head
        while curr:
            succ = curr.next
            curr.next = None
            #work to be done
            if curr.val <x:
                tails.next = curr
                tails = curr
                curr =succ
            else:
                taill.next = curr
                taill = curr
                curr =succ
        
        tails.next = sentinell.next
        return sentinels.next
                
                
            
        
        
        
        