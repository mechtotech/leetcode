class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        
        f(n) == no. of distinct ways to climb n step
        f(n) = f(n-1) + f(n-2) 
        
        DP=[0 for i in range(n+1)]
        
        DP[0] = 0
        DP[1] = 1
        DP[2]  = 2
        '''
        if n ==1 or n==2:
            return n
        
        DP= [0]*(n+1)
        DP[1] =1
        DP[2] =2
        
        for i in range(3,n+1):
            DP[i] = DP[i-1]+DP[i-2]
        
        return DP[n]
       
            