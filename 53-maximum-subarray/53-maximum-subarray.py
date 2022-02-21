class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # maximum subararry sum till index i f(i)
        # _ _ _ _ _ _
        # last didgit is f(n-1) +nums[i] 
        # nums[i]
        DP = [0 for i in range(len(nums))]
        
        DP[0] = nums[0]
        
        for i in range(1,len(nums)):
            DP[i] = max(DP[i-1]+nums[i],nums[i])
        return max(DP)
        