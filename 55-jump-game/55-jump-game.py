class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        f(i) = maximum index you can reach from index 0..i
        
        f(0) = nums[0]
        f(n) = max(DP[n-1],nums[i-1]+i)
        
        """
        if nums[0] ==0 and len(nums) !=1:
            return False
        n=len(nums)
        DP = [-1] * n
        DP[0] = nums[0]
        
        for i in range(1,n-1):
            DP[i] = max(DP[i-1],i+nums[i])
            
            if DP[i-1] < i:
                return False
        
        return DP[n-2] >= n-1
        
        
            
        

        
        