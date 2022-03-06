import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        result = []
        
        heapq.heapify(nums)
        
        while len(nums)!=0:
            result.append(heapq.heappop(nums))
        
        return result
        