class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        '''
        f(n) = min cost to reach n+1th step
        f(n) = f(n-1) + f(n-2)
        
        
        '''
        cost.append(0)
        n = len(cost)
        DP = [0 for i in range(n)]
        
        DP[0] = cost[0]
        DP[1] = cost[1]
        
        for i in range(2,n):
            DP[i] = min(DP[i-1],DP[i-2])+cost[i]
        
        return DP[n-1]
        
        