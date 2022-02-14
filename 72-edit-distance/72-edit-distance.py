class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        '''
        x1 x2 .... xm          xm      _        xm
        y1 y2 .... yn          _       yn       yn
        
        x1 x2 .... xm-1  xm    
        y1 y2 .... yn    _
        
        cost of alignment is equal to # insertion+ deletion + replace
        
        combine the sequnce together
        
        h - replaced to r
        o - match
        r - deleted
        s - match
        e- deleted
        
        pairwise alin them together with some gaps
        
        how many differernt ways to align these two stings together
        
        x1 x2 ... xm
        
        edit distance b/w x y
        f(i,j) = f(i-1,j
        
        
        '''
        m = len(word1)
        n = len(word2)
        DP = [[0 for i in range(n+1)] for j in range(m+1)]
        for row in range(1,m+1):
            DP[row][0] = row
        for col in range(1,n+1):
            DP[0][col] = col
        
        for row in range(1,m+1):
            for col in range(1,n+1):
                if word1[row-1]==word2[col-1]:
                    s = 0
                else:
                    s = 1
                DP[row][col] = min(DP[row-1][col]+1,DP[row][col-1]+1,DP[row-1][col-1]+s)
        return DP[-1][-1]
                
                
            
        
        
        
        
        
        