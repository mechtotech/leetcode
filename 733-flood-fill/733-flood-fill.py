class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        def bfs(x,y):
            q= deque()
            q.append((x,y))
            oldcolor = image[x][y]
            image[x][y] = color
            
            if color == oldcolor:
                return image
            
            while len(q) > 0:
                (r,c) = q.popleft()
                for row,col in neighbors(r,c):
                    if image[row][col] == oldcolor:
                        q.append((row,col))
                        image[row][col]= color
        def neighbors(row,col):
            result=[]
            if row-1 >= 0:
                result.append((row-1,col))
            if col-1 >=0:
                result.append((row,col-1))
            if row+1 < len(image):
                result.append((row+1,col))
            if col+1 < len(image[0]):
                result.append((row,col+1))
            return result
                        
        bfs(sr,sc)
        return image