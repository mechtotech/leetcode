class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m={}
        
        for i in range(len(nums)):
            if nums[i] in m:
                m[nums[i]] +=1
            else:
                m[nums[i]] = 1
        
        a = []
        
        for i in m:
            a.append(i)
            
        print(a)
        
        def helper(a,start,end,k):
            if start>=end:
                return
            
            pivot = random.randint(start,end)
            a[start],a[pivot] = a[pivot],a[start]
            
            orange = start
            for green in range(start+1,end+1):
                if m[a[green]] < m[a[start]]:
                    orange+=1
                    a[orange],a[green] = a[green],a[orange]
            a[orange],a[start] = a[start],a[orange]
            
            if len(a)-k==orange:
                return 
            elif len(a)-k < orange:
                helper(a,start,orange-1,k)
            else:
                helper(a,orange+1,end,k)
        
        helper(a,0,len(a)-1,k)
        return a[len(a)-k:]
        
                
        
        
            