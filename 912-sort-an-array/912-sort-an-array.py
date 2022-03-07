import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def helper(a,start,end):
            
            
            if start>= end:
                return
            
            pivot = random.randint(start,end)
            
            a[pivot], a[start] = a[start],a[pivot]
            
            orange = start
            
            for green in range(start+1,end+1):
                
                if a[green] < a[start]:
                    orange+=1
                    a[green],a[orange] = a[orange],a[green]
            
            a[orange],a[start] = a[start],a[orange]
            
            helper(a,start,orange-1)
            helper(a,orange+1,end)
        
        helper(nums,0,len(nums)-1)
        return nums
            
            
            
        
        
        
        
        
    
        