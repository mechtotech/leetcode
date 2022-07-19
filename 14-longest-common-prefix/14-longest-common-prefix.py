class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs.sort()
        
        strs_first = strs[0]
        strs_last = strs[-1]
        count= 0
        
        for i in range(len(strs_first)):
            
            if strs_first[i]==strs_last[i]:
                count+=1
            else:
                break
        if count == 0:
            return ""
        
        else:
            return strs_first[0:count]
            
            
        