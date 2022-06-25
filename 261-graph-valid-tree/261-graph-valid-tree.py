class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjlist = [[] for i in range(n)]
        for i,j in edges:
            adjlist[i].append(j)
            adjlist[j].append(i)
        
        
        visited = [-1]*n
        parent = [-1] *n
        
        def dfs(s):
            visited[s] =1
            parent[s] 
            for i in adjlist[s]:
                if visited[i]==-1:
                    visited[i] = 1
                    parent[i] = s
                    if dfs(i):
                        return True
                else:
                    if parent[s] != i:
                        return True
            return False
        def bfs(s):
            visited[s] = 1
            q =deque()
            q.append(s)
            while len(q) > 0:
                node = q.popleft()
                for i in adjlist[node]:
                    if visited[i] == -1:
                        visited[i] =1
                        parent[i] = s
                        q.append(i)
                    else:
                        if parent[s] != i:
                            return True
            return False
        
        count = 0
        for v in range(n):
            if visited[v] == -1:
                
                count+=1
                if count > 1:
                    return False
                if dfs(v):
                    return False
        return True
            
        
                    
        
            
        