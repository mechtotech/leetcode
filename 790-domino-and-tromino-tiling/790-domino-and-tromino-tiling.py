class Solution:
    def numTilings(self, n: int) -> int:
        """
        f(n) = no. of ways to tile 2 x n board
        
        f(n) = U(n-1) + L(n-1) + f(n-1)+f(n-2)
        
        
        XX     
        X  
        
        f(1) = 1
        f(2) = 2
        f(3) = 5
        
        
        
        """
        if n == 1 or n==2:
            return n
        if n == 3:
            return 5
        f = [0 for i in range(n+1)]
        u = [0 for i in range(n+1)]
        l = [0 for i in range(n+1)]
        
        f[1] = 1
        f[2] = 2
        
        
        l[1] = 1
        l[2] = 2
        
        u[1] = 1
        u[2] = 2
        
        for i in range(3,n+1):
            f[i] = f[i-1]+f[i-2] + l[i-2] + u[i-2]
            u[i] = f[i-1] + l[i-1]
            l[i] = f[i-1] +u[i-1]
           
        
        return f[n]%(10**9+7)
        
        
        
                
        
        
        
        
            
        