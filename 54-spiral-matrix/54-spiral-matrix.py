class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if len(matrix) == 1:
            return matrix[0]
        
        
        output = []
        
        visited=[[-1 for col in range(len(matrix[0]))] for row in range(len(matrix))]
        print(visited)
        
        def helper(row,col,direction):
            #if operation == "up":
# 		if row == 0 or arr[row-1][column] != 0:
			
# 			operation = "left"
# 			column -= 1
# 		else:
# 			#print('here')
# 			row -= 1

# 	elif operation == "down":
# 		if row == size-1 or arr[row+1][column] != 0:
# 			operation = "right"
# 			column += 1
# 		else:
# 			row += 1

# 	elif operation == "left":
# 		if column == 0 or arr[row][column-1] != 0:
# 			operation = "down"
# 			row += 1
# 		else:
# 			column -= 1

# 	elif operation == "right":
# 		if column == size-1 or arr[row][column+1] != 0:
# 			operation = "up"
# 			row -= 1
# 		else:
# 			column += 1
            
            visited[row][col] = 1
            output.append(matrix[row][col])
            
            if direction == "right":
                #print(col+1,len(matrix[0]))
                if col == len(matrix[0])-1 or visited[row][col+1] == 1:
                    direction = "down"
                    row+=1 
                else: #visited[row][col+1] ==-1:
                    #visited[row][col] ==1
                    #print(matrix[row][col])
                    col+=1
                    print(matrix[row][col])
            
            elif direction == "down":
                if row == len(matrix)-1 or visited[row+1][col] == 1:
                    direction = "left"
                    col-=1
                else:
                    #output.append(matrix[row][col])
                    #visited[row][col] ==1
                    row+=1
            
            elif direction == "left":
                if col == 0 or visited[row][col-1] == 1:
                    direction = "up"
                    row-=1
                else:
                   # output.append(matrix[row][col])
                    #visited[row][col] ==1
                    col-=1
            elif direction == "up":
                if row == 0 or visited[row-1][col] == 1:
                    direction = "right"
                    col+=1
                else:
                    #output.append(matrix[row][col])
                    #visited[row][col] ==1
                    row-=1
            
            
            
            if visited[row][col] == -1:
                helper(row,col,direction)
            
        helper(0,0,"right")
        return output
            
            
            
                    
            
        