class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        def helper(s,i,slate):
            if i ==len(s):
                result.append(slate[:])
                return
            
            
            m={}
            for pick in range(i,len(s)):
                if s[pick] not in m:
                    m[s[pick]] = 1
                    s[pick],s[i] = s[i],s[pick]
                    slate.append(s[i])
                    helper(s,i+1,slate)
                    slate.pop()
                    s[pick],s[i] = s[i],s[pick]
            
        helper(nums,0,[])
        return result
                
                
                    
                
        
                    
                    

                    
                    
                    
                
                
                
        
        
                
                
            
            
                
        
        
        
        