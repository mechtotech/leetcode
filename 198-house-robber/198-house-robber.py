class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        f(n) = maximum amount of money from 0...n-1 houses
        
        f(n) =  f(n-1),f(n-2) + nums[n]
        
        
        '''
        nums.append(0)
        n = len(nums)
        DP = [0]*n
        
        DP[0] = nums[0]
        DP[1] = max(nums[0],nums[1])
        
        for i in range(2,n):
            DP[i] = max(DP[i-1],DP[i-2]+nums[i])
        
        return DP[n-1]
            
        
        
        