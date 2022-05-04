class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        def helper(s,i,slate):
            
            
            
            if i == len(s):
                #slate.append(s[i])
                result.append(slate[:])
                #slate.pop()
            
            for j in range(i,len(s)):
                s[i],s[j] = s[j],s[i]
                slate.append(s[i])
                helper(s,i+1,slate)
                slate.pop()
                s[i],s[j] = s[j],s[i]
        
        helper(nums,0,[])
        return result
            
                
            
            
            
            
            
        
        