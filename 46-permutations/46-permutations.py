class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        def helper(s,i,slate):
            
            
            if i == len(s):
                result.append(slate[:])
                return
                
            
            for pick in range(i,len(s)):
                s[i],s[pick] = s[pick],s[i]
                slate.append(s[i])
                helper(s,i+1,slate)
                slate.pop()
                s[i],s[pick] = s[pick],s[i]
            
        helper(nums,0,[])
        return result
            
            
            
            
        
            
                
            
            
            
            
            
        
        