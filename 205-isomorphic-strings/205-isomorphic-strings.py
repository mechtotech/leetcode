class Solution:
    def isIsomorphic(self, a: str, b: str) -> bool:
        a_map = {} # mapping of each character in a to b
        b_map = {} # mapping of each character in b to a
        for index, character_a in enumerate(a):
            if character_a in a_map:
                if b[index] != a_map[character_a]:
                    return False
            else:
                a_map[character_a] = b[index]
                
            character_b = b[index]
            #print("Char a = ", character_a, " Char b =", character_b)

            #print("Map1 = ", a_map, " Map2 = ", b_map)

            if character_b  in b_map:
                if character_a != b_map[character_b]:
                    return False
            else:
                b_map[character_b] = character_a
            #print("Map1 = ", a_map, " Map2 = ", b_map)

        return True
            
        