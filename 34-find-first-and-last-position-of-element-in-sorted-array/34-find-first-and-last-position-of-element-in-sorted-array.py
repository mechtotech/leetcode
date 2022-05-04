class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) == 0:
            return [-1,-1]
        
        start = 0
        end = len(nums)-1
        first = -1
        
        while start <= end:
            mid = (start+end)//2
            
            if nums[mid] > target:
                end = mid-1
            elif nums[mid] < target:
                start = mid+1
            else:
                first = mid
                end = mid-1
        
        startl = 0
        endl = len(nums)-1
        last = -1
        while startl <= endl:
            mid = (startl+endl)//2
            
            if nums[mid] > target:
                endl = mid-1
            elif nums[mid] < target:
                startl = mid+1
            else:
                last = mid
                startl = mid+1
        
        return [first,last]
                
        
        
        
        
        
        
            
            
            
            
            
            
            
                
        
        
        