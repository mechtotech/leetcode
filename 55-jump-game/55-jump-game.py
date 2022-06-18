class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        f(i) # maximum index to jump from i
        
        f(i) = max(f(i-1),nums[i]+i)
        
        
        
        """
        
        if nums[0]==0 and len(nums)!=1:
            return False
        n = len(nums)   
        DP=[-1]*len(nums)
        
        
        DP[0] = nums[0]
        for i in range(1,n-1):
            DP[i] = max(DP[i-1],nums[i]+i)
            if DP[i] < i+1:
                return False
            
        
        return DP[n-2] >= n-1
            
        

        
        