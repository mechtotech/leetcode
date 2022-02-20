class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        '''
        f(n,sum) = min path sum from 0...n-1 rows
        
        
        '''
        n = len(triangle)
        
        DP= [None for i in range(n)]
        
        for row in range(n):
            DP[row] = [None]*(row+1)
        DP[0][0] = triangle[0][0]
        for row in range(1,n):
            DP[row][0] = triangle[row][0] + DP[row-1][0]
            DP[row][row] = triangle[row][row] + DP[row-1][row-1]


        for row in range(2,n):
            for col in range(1,row):
                DP[row][col] = min(DP[row-1][col],DP[row-1][col-1]) + triangle[row][col]
                
        return min(DP[n-1])
        
        
            
        
        
        
        
            
        