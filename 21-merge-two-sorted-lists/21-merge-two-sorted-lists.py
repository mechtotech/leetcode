# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        sentinel = ListNode()
        tail = sentinel
        
        # take out the minimum of head of l1 or l2
        # create a new linked list which is sorted
        l1 =list1
        l2 = list2
        while l1 and l2:
            if l1.val <=l2.val:
                tail.next = l1
                tail = l1
                l1 = l1.next
                tail.next = None
            else:
                tail.next = l2
                tail = l2
                l2= l2.next
                tail.next = None
        while l1:
            tail.next = l1
            tail = l1
            l1 = l1.next
            tail.next = None
        while l2:
            tail.next = l2
            tail = l2
            l2= l2.next
            tail.next = None
        
        
        return sentinel.next
            
                