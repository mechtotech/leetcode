class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) == 0:
            return [-1,-1]
        
        start = 0
        end = len(nums)-1
        first = -1
        
        while start <= end:
            
            mid = (start+end)//2
            
            if nums[mid] == target:
                first = mid
                end = mid-1
            
            elif nums[mid] > target:
                end = mid-1
            else:
                start = mid+1
            
        start = 0
        end = len(nums)-1
        last =-1
        while start <=end:
            mid = (start+end)//2
            
            if nums[mid] == target:
                last = mid
                start = mid+1
            elif nums[mid] > target:
                end = mid-1
            else:
                start = mid+1
            
        return [first,last]
                
                
        

            
            
            
            
            
            
                
        
        
        