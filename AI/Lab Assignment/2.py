N=4
def output(list):
    for i in list:
        for j in i:
            print(str(j)+" ",end=" ")
        print (" ")

def isValid(maze,x,y):
    if x>=0 and x<N and y>=0 and y<N and maze[x][y]==1:
        return False

def MazeSolution(maze):
    list=[[0 for j in range (4)]for i in range(4)]
    if Utility(maze,0,0,list)==False:
        print("no solution")
        return False  
    output(list)
    return True

def Utility(maze,x,y,list):
    if x==N-1 and y==N-1 and maze[x][y]==1:
        list[x][y]=1
        return True
    if isValid(maze,x,y)==True:
        list[x][y]=N-1
        
        if Utility(maze,x+1,y,list)==True:
            return True
        if Utility(maze,x,y+1,list)==True:
            return True
        list[x][y]=0
        return False
        

maze=[[1,0,0,0],
      [1,1,0,1],
      [0,1,0,0],
      [1,1,1,1]]
MazeSolution(maze)
