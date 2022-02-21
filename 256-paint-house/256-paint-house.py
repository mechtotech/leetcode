class Solution:
    def minCost(self, cost: List[List[int]]) -> int:
        '''
        _ _ _ _ _ 
        1.......n 
        
        f(n) = minimum cost to paint 0..n-1 houses 
        blue(n) = minimum cost to paint 0...n-1 houses with n-1 house painted as blue
        green(n)
        red(n)
        
        f(n) = min(blue(n),green(n),red(n))
        
        red = 1D array of length ==len(costs) = min(green(i-1),blue(i-1))
        
        blue = 
        
        red[0] = cost[0][0]
        blue[0] = cost[0][1]
        green[0] = cost[0][2]
        
        
        for i in range(1,len(costs)):
        blue[i] = min(green[i-1],red[i-1])
        green[i]====
        red[i]====
        
        return min()
        
        
        
        
        '''
        n= len(cost)
        blue = [0 for i in range(n)]
        green= [0 for i in range(n)]
        red = [0 for i in range(n)]
        
        blue[0] = cost[0][1]
        green[0] = cost[0][2]
        red[0] = cost[0][0]
        
        for i in range(1,n):
            blue[i] = min(green[i-1],red[i-1]) + cost[i][1]
            green[i] = min(blue[i-1],red[i-1]) + cost[i][2]
            red[i] = min(blue[i-1],green[i-1]) + cost[i][0]
            
        return min(blue[n-1],green[n-1],red[n-1])
        
        
        
        
        
        
       