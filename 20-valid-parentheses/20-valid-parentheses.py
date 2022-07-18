class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s)%2 == 1:
            return False
        
        stack = []
        
        
        map = { ")": "(", "}": "{", "]": "["}
        
        for i in s:
            
            if i not in map:
                
                stack.append(i)
            
            else:
                
                popped = stack.pop() if stack else '#'
                
                if map[i] != popped:
                    return False
        
        
        return not stack
            
        
        