class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        m ={}
        
        for i in range(len(nums)):
            n2 = target-nums[i]
            
            if n2 not in m:
                m[nums[i]]  = i
            else:
                return [i,m[n2]]
        
    
        
        