class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        robber 
        
        circular arrangement needs to converted to linear arrangement
        
        0...n-1 houses
        
        case 1) if 0 house gets robbed 
        
        then our linear arrangement becomes 2...n-2
        
        case 2) 0...n-1 incase first house is not robbed
        
        
        
        '''
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0], nums[1])
        if len(nums)==3:
            return max(nums[0],nums[2],nums[1])
        if len(nums)==4:
            return max(nums[0]+nums[2],nums[1]+nums[3])
        DP = [None for i in range(len(nums))]
        
        
        
        DP[2]= nums[2]
        DP[3] = max(nums[2],nums[3])
        
        for i in range (4,len(nums)-1):
            DP[i]=max(nums[i]+DP[i-2],DP[i-1])
        
        case1= nums[0]+DP[len(nums)-2]
            
            
       
        DP[1] = nums[1]
        DP[2]= max(nums[1],nums[2])
        
        for i in range(3,len(nums)):
            DP[i] = max(nums[i]+DP[i-2],DP[i-1])
        case2 = DP[len(nums)-1]
        
        return max(case1,case2)
        
        
        
        
        
        
        
        
        
        
        
        
        