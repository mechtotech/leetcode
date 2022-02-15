class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        '''
        a b c d e
        a _ c _ e
        
        cost of deletion is zero
        cost of match is one
        
        
        '''
        
        m = len(text1)
        n = len(text2)
        
        DP = [[0 for i in range(n+1)] for j in range(m+1)]
        
        for row in range(1,m+1):
            for col in range(1,n+1):
                if text1[row-1]==text2[col-1]:
                    s=1
                else:
                    s=0
                
                DP[row][col] = max(DP[row-1][col],DP[row][col-1],DP[row-1][col-1]+s)
        
        return DP[-1][-1]
       
    
    
        