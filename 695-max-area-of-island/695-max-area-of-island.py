class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visited = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
        
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
        
        #def bfs(row,col):
            #visited[row]
            
           
        def dfs(row,col):
            visited[row][col] =1
            area = 1
            for r,c in neighbor(row,col):
                if visited[r][c] == -1 and grid[r][c]==1:
                    visited[r][c] =1
                    area+=dfs(r,c)
            return area
        def bfs(row,col):
            visited[row][col] =1
            q= deque()
            q.append((row,col))
            area =1
            while len(q) > 0:
                r,c = q.popleft()
                
                for x,y in neighbor(r,c):
                    if visited[x][y] == -1 and grid[x][y] == 1:
                        visited[x][y] =1
                        q.append((x,y))
                        area+=1
            return area
                        
                        
        
        
        maxarea = 0 
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if visited[row][col] == -1 and grid[row][col]==1:
                    area = bfs(row,col) 
                    maxarea = max(maxarea,area)
        return maxarea
    
    
    
                    
            
            
            
            
            
        
        
                    
            
            
                    
                    
                    
                    
                
            
        
        
        