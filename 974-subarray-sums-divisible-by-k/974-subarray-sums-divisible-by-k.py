class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        m ={}
        
        prefixsum = 0
        total =0
        m[0] = 1
        
        for i in range(len(nums)):
            prefixsum = (prefixsum + nums[i]) %k
            
            if prefixsum in m:
                total +=m[prefixsum]
                
            if prefixsum in m:
                m[prefixsum] +=1
            else:
                m[prefixsum] =1
        
        return total
        