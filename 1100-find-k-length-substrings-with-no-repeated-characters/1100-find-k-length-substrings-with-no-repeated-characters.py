class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        
        """
        havefee
         -----
        m={h,a,v,e,f}
    
        """
        if k>len(s):
            return 0
        m = {}
        for i in range(k):
            if s[i] in m:
                m[s[i]] +=1
            else:
                m[s[i]] = 1
        total = 0
        if len(m) == k:
            total = 1
        else:
            total = 0
            
        
        for i in range(k,len(s)):
            if s[i] in m:
                m[s[i]] +=1
            else:
                m[s[i]] = 1
            m[s[i-k]]-=1
            if m[s[i-k]]==0:
                del m[s[i-k]]
            if len(m) == k:
                total +=1
        
        return total
                
            
                
                
            
        
        