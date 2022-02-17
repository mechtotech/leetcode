class Solution:
    def numTilings(self, n: int) -> int:
        '''
        f(n) = number of ways to tile 2 xn board
        f(n-1) = number of ways to tile 2 x(n-1) board
        
        x    xx
        x    xx   
        
        xx   x
        x   xx
        
        u(n) = -------
               ------
        f(n) = f(n-1) + u(n-2) +l(n-2) +f(n-2)
        
        u(n) = f(n-1) + l(n-1)
        l(n) = f(n-1) +u(n-1)
        
        '''
        if n ==1 or n==2:
            return n
        
        F = [None]*(n+1)
        L= [None]*(n+1)
        U = [None]*(n+1)
        
        F[1]= 1
        F[2] = 2
        
        
        L[1] = 1
        L[2] = 2
        U[1] =1
        U[2] =2
        
        for i in range(3,n+1):
            F[i] = F[i-1]+F[i-2]+L[i-2]+U[i-2]
            L[i] = F[i-1] + L[i-1]
            U[i] =F[i-1] +U[i-1]
        return F[n]%(10**9+7)
            
                
        
        
        
        
            
        