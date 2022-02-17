class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        '''
        _ _ _ _ _ _ _
        
        9 9 8 7
        
        
        
        
        
        '''
        if n ==0:
            return 1
        DP=[0 for i in range(n+1)]
        DP[1] = 9
        globalbox = 10
        for i in range(2,n+1):
            DP[i] = DP[i-1]*(11-i)
            globalbox+= DP[i]
        
        return globalbox
        