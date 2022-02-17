class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        DP = [[None for col in range(n)] for row in range(m)]
    
    
    
        for col in range(n):
            DP[0][col] =1
        for row in range(m):
            DP[row][0] =1
        
        for row in range(1,m):
            for col in range(1,n):
                DP[row][col] = DP[row-1][col]+DP[row][col-1]
    
    
    
    
    
    
    
    
        return DP[m-1][n-1]
        
        