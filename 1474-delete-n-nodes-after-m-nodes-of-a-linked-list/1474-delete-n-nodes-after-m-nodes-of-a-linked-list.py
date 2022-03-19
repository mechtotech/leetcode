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
            index= 0
            while curr and index !=m:
                prev = curr
                curr = curr.next
                index+=1
            index = 0
            p = curr
            while p and index != n:
                p = p.next
                index+=1
            
            prev.next = p
            curr = p
        
        return sentinel.next
            
        
# first move prev and curr pointer to m & m+1 postion 
# prev node is actually pointing sentinel
# curr node is actually poinring to head

# when curr is at m+1 postion we start a pointer p from curr.next to move to m+n+1 node
# prev.next = p
# curr= p


        
