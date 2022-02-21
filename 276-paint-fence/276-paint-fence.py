class Solution:
    def numWays(self, n: int, k: int) -> int:
        
        same= [None]*n
        different= [None]*n
        total = [None]*n
        # no of posts are only 1 i.e. n=0
        same[0] = 0
        different[0] = k
        total[0] = k
        
        for i in range(1,n):
            same[i] = different[i-1]
            different[i] = total[i-1] * (k-1)
            total[i] = same[i]+different[i]
        
        return total[n-1]
        
        '''
        _ _ _ _ _
        1.......n fences
        
        total(n) = # number if ways to paint fence 0..n 
        different(i)= case 1 # number if ways to paint fence 0..n where the color last n-1 & n  fence are different
        same(i)= # number if ways to paint fence 0..n where the color of  is similar to fence n-1
        
        f(i) = same(i) + different(i)
        same(i) = different(i-1)
        different(i) = total[i-1]*(k-1)
        total = different(i-1) + total(i-1)*(k-1)
        same(i) = 1D array equal to n
        different 
        total(i) = 1D array equal to n
        
        same(0) = 0
        different(0)  = k
        
        
        
        
        
        
        
        
        '''