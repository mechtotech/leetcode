class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        i = 0
        j = len(nums)-1
        result = []
        
        while i <= j:
            
            if nums[i] + nums[j] == 2* target and nums[i] == target:
                result.append(i)
                result.append(j)
                break
            elif nums[i] + nums[j] > 2* target:
                j-=1
            else:
                i+=1
        
        
        return result if len(result) != 0 else [-1,-1]
                
                
                
        
        
        