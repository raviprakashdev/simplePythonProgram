# Program to multiply two matrices using nested loops 
  
# take a 3 by 3 matrix 
A = [[1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]] 
  
# take a 3 by 4 matrix     
B = [[100, 200, 300, 400], 
    [500, 600, 700, 800], 
    [900, 1000, 1100, 1200]] 
      
result = [[0, 0, 0, 0], 
        [0, 0, 0, 0], 
        [0, 0, 0, 0]] 
  
# iterating by row of A 
for i in range(len(A)): 
  
    # iterating by coloum by B  
    for j in range(len(B[0])): 
  
        # iterating by rows of B 
        for k in range(len(B)): 
            result[i][j] += A[i][k] * B[k][j] 
  
for r in result: 
    print(r) 
