class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        if len(nums) <2:
            return 0
        nums.sort()
        
        i = 0
        j = 1
        maxdiff = -float('inf')
        while j < len(nums):
            maxdiff = max(maxdiff,nums[j]-nums[i])
            i+=1
            j+=1
        
        return maxdiff
        
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        