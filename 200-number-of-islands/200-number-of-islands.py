class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
        
        def dfs(row,col):
            visited[row][col] = 1
            for (r,c) in neighbor(row,col):
                if visited[r][c] == -1 and grid[r][c] == '1':
                    visited[r][c] = 1
                    dfs(r,c)
                    
            
        
        def neighbor(row,col):
            result = []
            
            if row-1 >= 0:
                result.append((row-1,col))
            if row+1<len(grid):
                result.append((row+1,col))
            if col-1 >= 0:
                result.append((row,col-1))
            if col+1 < len(grid[0]):
                result.append((row,col+1))
            return result
        
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if visited[row][col] == -1 and grid[row][col] == '1':
                    count+=1
                    dfs(row,col)
        return count
        
        #def bfs(x,y):
            
        
                
                
                
            
            
            
                    
        
                
        
        
        
        
        