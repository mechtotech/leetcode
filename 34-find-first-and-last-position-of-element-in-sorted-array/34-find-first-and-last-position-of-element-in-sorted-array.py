class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) == 0:
            return [-1,-1]
        
        
        i = 0
        j = len(nums)-1
        first = -1
        
        
        while i <= j:
            mid = (i+j)//2
            if nums[mid] < target:
                i = mid+1
            elif nums[mid] >target:
                j = mid -1
            else:
                first = mid
                j = mid-1
        
        i = 0
        j = len(nums)-1
        last = -1
        
        while i <= j:
            mid = (i+j)//2
            if nums[mid] < target:
                i = mid+1
            elif nums[mid] > target:
                j = mid-1
            else:
                last = mid
                i = mid+1
        return [first,last]
        
        
        
        
        
        
        
        
            
            
            
            
            
            
            
                
        
        
        