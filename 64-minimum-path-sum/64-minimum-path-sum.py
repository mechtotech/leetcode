class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        '''
        f(m,n) = minimum path to get to m,n
        
        f(m,n) depends on f(m-1,n),f(m,n-1)
        f(m,n) = min(f(m-1,n), f(m,n-1))+grid[m][n]
        '''
        m = len(grid)
        n = len(grid[0])
        DP = [[0 for col in range(n)] for row in range(m)]
        DP[0][0] = grid[0][0]
        for row in range(1,m):
            DP[row][0] = DP[row-1][0] + grid[row][0]
        for col in range(1,n):
            DP[0][col] = DP[0][col-1] + grid[0][col]
        
        
        for row in range(1,m):
            for col in range(1,n):
                DP[row][col] = min(DP[row-1][col],DP[row][col-1])+ grid[row][col]
        
        return DP[m-1][n-1]
        