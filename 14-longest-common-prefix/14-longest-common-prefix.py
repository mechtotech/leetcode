class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        
        string_first = strs[0]
        string_last = strs[-1]
        count=0
        for i in range(len(string_first)):
            if string_first[i] == string_last[i]:
                count+=1
            else:
                break
        if count == 0:
            return ""
        else:
            return string_first[0:count]
                
        
        