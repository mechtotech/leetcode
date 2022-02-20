class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        
        f(n) = maximum amount you can rob from n-1 houses
        
        f(n) = max of f(n-1) or f(n-2)+nums[n]
        
        case1 when house 0 is  robbed
        0 & n-1 next to eachother      0 1 2 3 4 
        nums[2.....n-2]
        
        
        
        case 2 when house 0 is not robbed
        1....n-1
        '''
        
        n= len(nums)
        
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n==2:
            return max(nums[1],nums[0])
        if n==3:
            return max(nums[0],nums[1],nums[2])
        if n==4:
            return max(nums[0]+nums[2], nums[1]+nums[3])
        
        DP = [None] * n
        #case1:
        
        DP[2] = nums[2]
        DP[3] = max(nums[2],nums[3])
        for i in range(4,n):
            DP[i] = max(DP[i-1],DP[i-2]+nums[i])
        
        case1 = DP[n-2] +nums[0]
        #case2:
        DP[1] = nums[1]
        DP[2] = max(nums[1],nums[2])
        for i in range(3,n):
            DP[i] = max(DP[i-1],DP[i-2]+nums[i])
        case2 = DP[n-1]
        
        
        return max(case1,case2)
        
        
        
        
        
            
        
    
        
        