class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        f(n) # number of distinct to climb n steps
        f(n) = f(n-1 + f(n-2)
        
        '''
        
        if n <=2:
            return n
        else:
            DP = [0 for i in range(n+1)]
        
            DP[1] = 1
            DP[2] = 2
            
            for i in range(3,n+1):
                DP[i] = DP[i-1]+DP[i-2]
            
            return DP[n]