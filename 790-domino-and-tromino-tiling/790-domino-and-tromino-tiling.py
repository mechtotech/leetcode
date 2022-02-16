class Solution:
    def numTilings(self, n: int) -> int:
        '''
        2 xn tiles f(n)
        last tile can covered with 1 tile | f(n-1)   =  f(n-2) 
        or _|   =  L(n-2) = |||||  ||||-  L(n) = f(n-1) + U(n-1)
        L(n-2) = f(n-3) + U(n-3)
        |-  = U(n-2) ||||..|_ U(n) = f(n-1)+ L(n-2
        
        f(n) = f(n-1)+L(n-2)+U(n-2)+f(n-2)
        f(1) = 1
        f(2) = 2
        f(3)  =5
        
        f(1)--> f(2)
        l(1)---> l(2)
        u(1)---> u(2)
    
        
        
        
        '''
        
        DP=[None]*3
        L=[None]*3
        U = [None]*3
      
        
        if n <=2:
            return n
        
        else:
            DP[1] = 1
            DP[2] = 2
            L[1] =1
            U[1] = 1
            L[2] = 2
            U[2] = 2
            
            
            for i in range(3,n+1):
                DP[i%3] = (DP[(i-1)%3]+L[(i-2)%3]+U[(i-2)%3]+DP[(i-2)%3])
                L[i%3] = (DP[(i-1)%3]+ U[(i-1)%3])
                U[i%3] = (DP[(i-1)%3] + L[(i-1)%3])
                
            return DP[n%3]%((10**9)+7)
                
        
        
        
        
            
        