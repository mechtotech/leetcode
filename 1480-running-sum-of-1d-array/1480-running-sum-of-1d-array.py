class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefixsum = 0
        runningsum = []
        
        for i in range(len(nums)):
            prefixsum+=nums[i]
            runningsum.append(prefixsum)
        
        return runningsum
        