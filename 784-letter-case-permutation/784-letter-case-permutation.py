class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        
        result=[]
        def helper(s,i,slate):
            
            if i == len(s):
                result.append("".join(slate))
                return
            
            if s[i].isdigit():
                slate.append(s[i].upper())
                helper(s,i+1,slate)
                slate.pop()
            else:
                slate.append(s[i].upper())
                helper(s,i+1,slate)
                slate.pop()
                slate.append(s[i].lower())
                helper(s,i+1,slate)
                slate.pop()
        
        
        helper(s,0,[])
        return result
        
            
            
                
            
            
    
            
                
                
        