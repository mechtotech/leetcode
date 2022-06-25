class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adjlist = [[]for i in range(n)]
        
        for i,j in edges:
            adjlist[i].append(j)
            adjlist[j].append(i)
        
        visited = [-1]*n
        
        def dfs(s):
            visited[s] =1
            for i in adjlist[s]:
                if visited[i] == -1:
                    visited[i] = 1
                    dfs(i)
        
        count = 0
        for v in range(n):
            if visited[v] == -1:
                count+=1
                dfs(v)
                
        return count
                
                
        
        