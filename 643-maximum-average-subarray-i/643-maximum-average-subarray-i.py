class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowsum = sum(nums[:k])
        maxwindowsum = windowsum
        
        for i in range(k,len(nums)):
            windowsum += nums[i]-nums[i-k]
            maxwindowsum = max(windowsum,maxwindowsum)
            
        return maxwindowsum/k
    
    
    
    
            
        
        
        