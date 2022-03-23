class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        
        00011122_
          0  1  i
        """
        i = 0
        zero = -1
        one = -1
        
        
        while i < len(nums) and zero < len(nums) and one < len(nums):
            
            if nums[i] == 2:
                i+=1
            elif nums[i] == 1:
                one+=1
                nums[one],nums[i] = nums[i],nums[one]
                i+=1
            elif nums[i] == 0:
                one+=1
                nums[one],nums[i] = nums[i],nums[one]
                zero+=1
                nums[one],nums[zero] = nums[zero],nums[one]
                i+=1
        return nums
                
                
            
            
            
        