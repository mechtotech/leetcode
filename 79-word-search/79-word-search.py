class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        result = [False]
        visited = [[-1 for col in range(len(board[0]))] for row in range(len(board))]
        def dfs(s,i,row,col):
            if i == len(s):
                result[0] = True
                return
            for r,c in neighbor(row,col):
                if visited[r][c]==-1 and board[r][c] == s[i]:
                    visited[r][c] = 1
                    dfs(s,i+1,r,c)
                    visited[r][c] = -1
        
        def neighbor(row,col):
            result = []
            if row-1 >= 0:
                result.append((row-1,col))
            if row+1<len(board):
                result.append((row+1,col))
            if col-1 >= 0:
                result.append((row,col-1))
            if col+1 < len(board[0]):
                result.append((row,col+1))
            return result
 
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    visited[row][col] = 1
                    dfs(word,1,row,col) 
                    visited[row][col] = -1
                        
        return result[0]
        