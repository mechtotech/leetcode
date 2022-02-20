class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        DP = [0 for i in range(len(days))]
 
        DP[0] =min(costs) # lowest ticket cost
        for i in range(1,len(days)):
 
            case1 = DP[i-1] + costs[0]
 
 
            j = i-1
 
            while j >= 0 and days[j]>=days[i]-6:
                j -= 1
 
            if j >=0:
                case2 = DP[j] +  costs[1]
 
            else:
                case2=costs[1]
 
            j= i-1
 
            while j>=0 and days[j]>=days[i]-29:
                j-=1
            if j >=0:
                case3 = DP[j] +  costs[2]
 
            else:
                case3=costs[2]
 
            DP[i]=min(case1,case2,case3)
        return DP[len(days)-1]