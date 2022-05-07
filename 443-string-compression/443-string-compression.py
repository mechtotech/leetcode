class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = 0
        j = 0
        compressed=[]
        while i <len(chars):
            count = 0
            while j < len(chars) and chars[i] == chars[j]:
                j+=1
                count+=1
            
            if count <= 1:
                compressed+= chars[i]
                i=j
            else:
                compressed+=chars[i]
                compressed+=str(count)
                i=j
        chars[:] = list(compressed)
        return len(chars)
        
                
                
            
        