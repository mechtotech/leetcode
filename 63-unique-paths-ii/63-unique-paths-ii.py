class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        DP = [[0 for col in range(n)] for row in range(m)]
        
        if obstacleGrid[0][0] ==1 or obstacleGrid[m-1][n-1]==1:
            return 0
            
        
        DP[0][0] = 1
     
        for row in range(1,m):
            if obstacleGrid[row][0] !=1:
                DP[row][0] = 1
            else:
                break
        
        for col in range(1,n):
            if obstacleGrid[0][col] !=1:

                DP[0][col] = 1
            else:
                break
        
        
        for row in range(1,m):
            for col in range(1,n):
                if obstacleGrid[row][col] != 1:
                    DP[row][col] = DP[row-1][col]+DP[row][col-1]
        
        
        return DP[m-1][n-1]
    
            
        
        
        
        
        
        
                
        
        
        