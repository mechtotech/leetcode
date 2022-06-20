class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        """
        
        prefix sum 
        
        """
        
        hashmap={}
        globalcount = 0
        
        hashmap[0] = 1
        prefixsum = 0
        
        for i in range(0,len(nums)):
            prefixsum +=nums[i]
            
            if prefixsum-k in hashmap:
                globalcount += hashmap[prefixsum-k]
            
            if prefixsum in hashmap:
                hashmap[prefixsum] +=1
            else:
                hashmap[prefixsum] =1
        
        return globalcount 
            
        