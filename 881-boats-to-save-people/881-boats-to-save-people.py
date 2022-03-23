class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        arr=sorted(people)
        trip=0
        i=0
        j =len(arr)-1
        while i <= j:
            if arr[i]+arr[j] <= limit:
                trip+=1
                i+=1
                j-=1
            else:
                trip+=1
                j-=1
        return trip
        
        
        
        