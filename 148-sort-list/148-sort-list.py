# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def helper(h):
            if h is None or h.next is None:
                return h
            
            r = h
            t = h
            
            while r.next and r.next.next:
                r=r.next.next
                t=t.next
                
            h2 = t.next
            t.next = None
            
            list1 = helper(h)
            list2 = helper(h2)
            
            sentinel = ListNode()
            tail = sentinel
            
            while list1 and list2:
                if list1.val <= list2.val:
                    tail.next = list1
                    tail = list1
                    list1 = list1.next
                    tail.next = None
                    
                else:
                    tail.next = list2
                    tail = list2
                    list2 = list2.next
                    tail.next = None
                    
                    
            while list1:
                tail.next = list1
                tail = list1
                list1 = list1.next
                tail.next = None
            while list2:
                tail.next = list2
                tail = list2
                list2 = list2.next
                tail.next = None
            
            return sentinel.next
        return helper(head)