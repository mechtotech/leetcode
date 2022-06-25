class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """
        Bipartite is when there are odd length cycles
        
        when there is a cycle and its odd length return not bipartite
        
        """
        n = len(graph)
        
        visited = [-1]*n
        parent = [-1]* n
        setid = [-1]*n
        distance = [-1]*n
        
        def bfs(s):
            visited[s] = 1
            distance[s] = 0
            
            q = deque()
            q.append(s)
            while len(q) > 0:
                node =  q.popleft()
                for i in graph[node]:
                    if visited[i] == -1:
                        visited[i] =1
                        parent[i] = node
                        distance[i] = distance[node]+1
                        q.append(i)
                    else:
                        if parent[node] != i:
                            if distance[node] == distance[i]:
                                return False
            return True
        
        for v in range(n):
            if visited[v] == -1:
                if bfs(v) is False:
                    return False
        return True
                
                
            
            
    
    
        
        
        
        
                
                
        
        
        