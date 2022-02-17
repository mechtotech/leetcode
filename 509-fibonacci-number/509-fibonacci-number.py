class Solution:
    def fib(self, n: int) -> int:
        
        '''
        f(n) = f(n-1) + f(n-2)
        
        
        f(1) f(2)  f(3)
        
        '''
        if n <=1:
            return n
        else:
            DP=[0 for i in range(n+1)]
        
            DP[0] = 0
            DP[1] =1
        
            for i in range(2,n+1):
                DP[i] = DP[i-1]+DP[i-2]
        
            return DP[n]