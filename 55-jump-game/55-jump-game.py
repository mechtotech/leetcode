class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if nums[0] == 0 and len(nums) != 1:
            return False
        
        
        DP = [0] *len(nums)
        DP[0] = nums[0]
        
        for i in range(1,len(nums)-1):
            DP[i] = max(DP[i-1],nums[i]+i)
            if DP[i] < i+1:
                return False
            
            
        return DP[len(nums)-2] >= len(nums)-1
            