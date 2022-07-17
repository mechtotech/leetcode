class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        s=[]
        for i in range(1,n+1):
            s.append(i)
        result = []
        
        def helper(s,i,slate):
            
            if len(slate) == k:
                result.append(slate[:])
                return
            if i == n:
                return
            
            helper(s,i+1,slate)
            slate.append(s[i])
            helper(s,i+1,slate)
            slate.pop()
            
        
        helper(s,0,[])
        return result
            
            
        
        
        