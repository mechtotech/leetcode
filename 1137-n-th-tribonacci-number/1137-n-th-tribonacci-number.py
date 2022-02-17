class Solution:
    def tribonacci(self, n: int) -> int:
        
        '''
        f(n) = f(n-1)+f(n-2)+f(n-3)
        '''
        if n ==0:
            return 0
        elif n<=2:
            return 1
        else:
            DP=[0 for i in range(n+1)]
            DP[1]= 1
            DP[2] =1
            
            for i in range(3,n+1):
                DP[i] = DP[i-2]+DP[i-1]+DP[i-3]
            return DP[n]
        
        