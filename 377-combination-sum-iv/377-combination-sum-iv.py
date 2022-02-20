class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        '''
        t = 0
                     [1,2]    t = 3
                      t
                  t-1   t-2
                t-1-1    t-2-1 t-2-2
                t-1-1-1
                
        f(t) # ways to break target t with nums
        
        f(t) =    f(t-nums[i]) where i varies 0 to len(nums)-1
        
              0 1 2 3             1
              _ _ _ _ _ 
              0 1 2 3 4 
        
        
        '''
        
        
        DP = [0 for i in range(target+1)]
        DP[0] = 1
        
        for i in range(1,target+1):
            for n in nums:
                if i-n>=0:
                    DP[i] += DP[i-n]
        return DP[target] 
                    
                    
                
                
        
        
        