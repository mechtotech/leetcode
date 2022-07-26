class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
        strs.sort()
        
        first = strs[0]
        last = strs[-1]
        count = 0
        for i in range(len(first)):
            if first[i] == last[i]:
                count+=1
            else:
                break
        
        if count == 0:
            return ""
        
        return first[:count]
            
            
        
        
 
        
        
            
            
        