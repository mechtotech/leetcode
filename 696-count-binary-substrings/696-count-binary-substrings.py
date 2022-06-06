class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = [1]
        for i in range(1,len(s)):
            if s[i-1] == s[i]:
                groups[-1]+=1
            else:
                groups.append(1)
        result = 0
        for i in range(1,len(groups)):
            result+= min(groups[i-1],groups[i])
        return result
            
        
            
                
                
                
            
                
            
                
        
        