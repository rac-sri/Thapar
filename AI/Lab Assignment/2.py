N = 4
def printSolution( sol ): 
      
    for i in sol: 
        for j in i: 
            print(str(j) + " ", end ="") 
        print("") 
  
def isSafe( maze, x, y ): 
      
    # function to check if it is safe to continue execution
    if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1: 
        return True
      
    return False
  
def solveMaze( maze ): 
      
    # create a 4x4 matrix
    sol = [ [ 0 for j in range(4) ] for i in range(4) ] 
      
    if solveMazeUtil(maze, 0, 0, sol) == False: 
        print("Solution doesn't exist"); 
        return False
      
    printSolution(sol) 
    return True
      
def solveMazeUtil(maze, x, y, sol): 
    printSolution(sol)
    print("\n")
    if x == N - 1 and y == N - 1 and maze[x][y]== 1: 
        sol[x][y] = 1
        return True
          
    if isSafe(maze, x, y) == True:
         
        sol[x][y] = 1

        # going down row wise
        if solveMazeUtil(maze, x + 1, y, sol) == True:
            return True
        
        # going along the row ( dfs )
        if solveMazeUtil(maze, x, y + 1, sol) == True:
            return True
        
        sol[x][y] = 0
        return False
  
if __name__ == "__main__": 
    # rat's route data
    maze = [ [1, 0, 0, 0], 
             [1, 1, 0, 1], 
             [0, 1, 0, 0], 
             [1, 1, 1, 1] ] 
               
    solveMaze(maze)