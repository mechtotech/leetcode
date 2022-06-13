class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        windowsum = 0
        globalans = float('inf')
        left = 0
        
        for i in range(len(nums)):
            windowsum += nums[i]
            while left  <= i and windowsum >= target:
                windowsum -= nums[left]
                globalans = min(globalans,i-left+1)
                left+=1
        
        if globalans == float('inf'):
            return 0
        else:
            return globalans
            
            
        
        