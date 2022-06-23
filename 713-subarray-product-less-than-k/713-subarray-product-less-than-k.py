class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        """
        
        __ __ __ __ __ __ __
                           i
               l
        
        nums[l:i+1] is product greater than  k
        
        globalcount +=1
        
        
        
        
        number of subarray with products less than k that ends at i
        
        global answer is equal to sum of all local answers
        
        
        
        
        
        """
        left = 0
        windowproduct  = 1
        globalcount = 0
        
        for i in range(len(nums)):
            windowproduct*=nums[i]
            
            while left <= i and windowproduct >= k:
                windowproduct /=nums[left]
                
                left+=1
            globalcount +=(i-left+1)
        return globalcount
    
        
        
        
        