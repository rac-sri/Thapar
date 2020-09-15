import sys
import copy

q = []
visited = []

def compare(s,g):
    if s==g:
        return(1)
    else:
        return(0)

def find_pos(s):
    for i in range(3):
        for j in range(3):
            if s[i][j] == 0:
                return([i,j])

def up(s,pos):
    i = pos[0]
    j = pos[1]

    if i>0:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i-j][j]
        temp[i-j][j] = 0
        return temp
    else :
        return (s)

def down(s,pos):
    i = pos[0]
    j = pos[1]
    if i < 2:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i+1][j]
        temp[i+1][j] = 0
        return (temp)
    else:
        return (s)

def right(s,pos):
    i = pos[0]
    j = pos[1]
    if j < 2:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i][j+1]
        temp[i][j+1] = 0
        return (temp)
    else:
        return (s)

def left(s,pos):
    i = pos[0]
    j = pos[1]
    if j > 0:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i][j-1]
        temp[i][j-1] = 0
        return (temp)
    else:
        return (s)

def enqueue(s,val,val1):
    global q
    if val<val1:
        q = q + [(val,s)]

def heuristic(s,g):
    d = 0
    for i in range(3):
        for j in range(3):
            if s[i][j] != g[i][j]:
                d += 1
    return d

def dequeue(g):
    global q
    global visited
    visited = visited + [q[0][1]]
    elem = q[0][1]
    del q[0]
    return (elem)


def search(s,g):
    curr_state = copy.deepcopy(s)
    if s == g:
        return

    global visited
    while(1):
        pos = find_pos(curr_state)
        new = up(curr_state,pos)
        val1=heuristic(s,g)
        if new != curr_state:
            if new == g:
                print ("found!! The intermediate states are:")
                print (visited + [g])
                return
            else:
                if new not in visited:
                    enqueue(new,heuristic(new,g),val1)
        new = down(curr_state,pos)
        if new != curr_state:
            if new == g:
                print ("found!! The intermediate states are:")
                print (visited + [g])
                return
            else:
                if new not in visited:
                    enqueue(new,heuristic(new,g),val1)

        new = right(curr_state,pos)
        if new != curr_state:
            if new == g:
                print ("found!! The intermediate states are:")
                print (visited + [g])
                return
            else:
                if new not in visited:
                    enqueue(new,heuristic(new,g),val1)
        
        new = left(curr_state,pos)
        if new != curr_state:
            if new == g:
                print ("found!! The intermediate states are:")
                print (visited + [g])
                return
            else:
                if new not in visited:
                    enqueue(new,heuristic(new,g),val1)

        if len(q) > 0:
            curr_state = dequeue(g)
        else:
            print ("not found")
            return

def main():
    s = [[2,8,3],[1,5,4],[7,6,0]]
    g = [[1,2,3],[8,0,4],[7,6,5]]
    global q
    global visited
    visited = visited + [s]
    search(s,g)

if __name__ == "__main__":
    main()