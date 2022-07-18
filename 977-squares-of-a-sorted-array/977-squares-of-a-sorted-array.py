class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        
        
        result = [0] * len(nums)
        i = 0
        j = len(nums) - 1
        for k in range(len(nums) - 1, -1, -1):
            if abs(nums[i]) < abs(nums[j]):
                square = nums[j]
                j -= 1
            else:
                square = nums[i]
                i += 1
            result[k] = square * square
        return result