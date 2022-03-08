import heapq
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        heap = nums[:k]
        
        heapq.heapify(heap)   
        
        for i in range(k,len(nums)):
            
            if heap[0] < nums[i]:   #o(1)
                heapq.heappushpop(heap,nums[i])  #o(logk) insert  # o(logk) extract min
        
        return heap[0]
        
                
            