class Solution:
    def integerBreak(self, n: int) -> int:
        '''
        
        _ _ _ _ _ _ _
        
        1...n  but we have condtion to break the interger into 2 parts 1, n-1
        
        1..n-1
        f(i) = max(f(j) *f(i-j)) where j varies from 1 to i represents
        
        f(i) = f(1) f(2)
        
        f(1) = 1
        f(2) = 2
        
        f(5) = f(3)* f(2)  we have f(2) =2
        
        
        f(1) f(2) f(3) ... f(n)
        
        options to come out 
        
        in order of fill last element in 1....n-1
        
        
        '''
        if n==2:
            return 1
        DP = [0 for i in range(n+1)]
        
        DP[1] = 1
        DP[2] = 2
        for i in range(3,n+1):
            if i == n:
                DP[i] = n-1
            else: 
                DP[i] = i
            for j in range(1,i):
                DP[i] = max(DP[j]*DP[i-j],DP[i])
            
                
        return DP[n]
        