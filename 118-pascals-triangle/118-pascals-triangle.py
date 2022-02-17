class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        
        
        DP= [None]*(numRows)
        for row in range(numRows):
            DP[row] = [None]*(row+1)
        DP[0][0] =1 
        for row in range(1,numRows):
            DP[row][0] = 1
            DP[row][row] =1
        for row in range(2,numRows):
            for k in range(1,row):
                DP[row][k] = DP[row-1][k]+DP[row-1][k-1]
        return DP
            