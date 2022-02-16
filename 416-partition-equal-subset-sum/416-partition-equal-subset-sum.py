class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        '''
        first of all we need to find if sum of 2 subset to be equal hence the total sum must be even
        
        
        k = total/2
        target
        as a lazy manager i can make the decision for only last number
        f(n,k) is boolean for subset for n numbers adding upto k (True or False)
        depends on boolean of 
        Inclusion where we include the last number in the subset and find n-1 numbers adding upto k-last number
        Exclusion where we exclude the last number in the subset and find n-1 numbers adding upto k 
        
        f(n,k) = f(n-1,k) or f(n-1,k-nth number)
        
        '''
        
        if sum(nums)%2 !=0:
            return False
        
        k = sum(nums)//2
        n= len(nums)
        DP = [[True for i in range(k+1)]for j in range(n+1)]
        
        for j in range(1,k+1):
            DP[0][j] = False
        
        for i in range(1,n+1):
            for j in range(1,k+1):
                DP[i][j] = DP[i-1][j]
                if j >= nums[i-1]:
                    DP[i][j] = DP[i-1][j] + DP[i-1][j-nums[i-1]]
        
        return DP[-1][-1]
                    
        