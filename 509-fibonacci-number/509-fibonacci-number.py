class Solution:
    def fib(self, n: int) -> int:
        
        """
        f(n) = f(n-1)+f(n-2)
        
        f(n-2)   f(n-1)   f(n)        
        """
        
        if n == 0 or n==1:
            return n
        
        
        
        a = 0
        b =1
        c=0
        for _ in range(2,n+1):
            c = a+b
            a= b
            b= c
        
        return c
            
            
            