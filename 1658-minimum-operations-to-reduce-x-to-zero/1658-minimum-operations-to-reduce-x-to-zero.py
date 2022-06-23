class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        """
        if sum(nums) < x:
        return -1
        k= sum-x
        
        for minmizing the operator 
        maximum subarry has to be max
        for maxim subarray with sum >=k
        _ _ _ _ _ _
        0   l     i
        
        max(len(nums[left:i+1]))
        len nums -len(nums[left:i+1])
        
        
        """
        if sum(nums) <x:
            return -1
        left = 0
        windowsum = 0
        globalcount=-1
        k= sum(nums)-x
        
        for i in range(len(nums)):
            windowsum += nums[i]
            while left <= i and windowsum > k:
                windowsum -= nums[left]
                left+=1
            
            if windowsum == k:
                globalcount = max(globalcount,i-left+1)
        
        if globalcount==-1:
            return -1
        else:
            return len(nums)-globalcount
        