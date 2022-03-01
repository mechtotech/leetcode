class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        
         _ _ _ _ _ _
                   n
         
         if odd
         
         3 < 5 > 2 is odd 
         0   1   2
         
        """
        n = len(nums)
        for i in range(1,n):
            if (i%2 == 0 and nums[i-1]  < nums[i]) or (i%2!=0 and nums[i-1] > nums[i]):
                nums[i-1],nums[i] = nums[i],nums[i-1]
        
        return nums
         
        