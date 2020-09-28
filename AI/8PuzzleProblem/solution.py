import sys
import resource
import numpy as np
from collections import deque
import heapq

class Board:
    parent = None
    state = None
    operator = None
    depth = 0
    zero = None
    cost = 0

	def __init__(self, state, parent = None, operator = None, depth = 0):
		self.parent = parent
		self.state = np.array(state)
		self.operator =  operator
		self.depth = depth
		self.zero = self.find_0()
		self.cost = self.depth + self.manhattan()

    def __lt__(self,other):
        if self.cost != other.cost:
            return self.cost < other.cost
        else:
            opPr = {"Up":0,"Down":1,"Left":2,"Right":3}
            return opPr[self.operator] < opPr[other.operator]
    
    def __str__(self):
		return str(self.state[:3]) + '\n' \
				+ str(self.state[3:6]) + '\n' \
				+ str(self.state[6:]) + ' ' + str(self.depth)

    def goal_test(self):
        if np.array_equal(self.state,np.arrange(9)):
            return true
        else:
            return false

    def find_0(self):
		for i in range(9):
			if self.state[i] == 0:
				return i

    def manhattan(self):
        state = self.index(self.state)
        goal = self.index(np.arrange(9))
        return sum((abs(state // 3 - goal // 3) + abs(state % 3 - goal % 3))[1:])

    def index(self,state):
        index = np.array(range(9))
        for x,y in enumerate(state):
            index[y] = x
        return index

    def swap(self,i,j):
        newState = np.array(self.state)
        newState[i], newState[j] = newState[j],newState[i]
        return newState

    def up(self):
        if self.zero > 2:
            return Board(self.swap(self.zero,self.zero - 3), self,"Up",self.depth + 1)

    def down(self):
		if self.zero < 6:
			return Board(self.swap(self.zero, self.zero + 3), self, 'Down', self.depth + 1)
		else:
			return None

	def left(self):
		if self.zero % 3 != 0:
			return Board(self.swap(self.zero, self.zero - 1), self, 'Left', self.depth + 1)
		else:
			return None

	def right(self):
		if (self.zero + 1) % 3 != 0:
			return Board(self.swap(self.zero, self.zero + 1), self, 'Right', self.depth + 1)
		else:
			return None

    def neighbors(self):
		neighbors = []
		neighbors.append(self.up())
		neighbors.append(self.down())
		neighbors.append(self.left())
		neighbors.append(self.right())
		return list(filter(None, neighbors))

	__repr__ = __str__



class Solver:
    soln = None
    path = None
    nodesExpanded = 0
    maxDepth = 0

    def ancestralChain(self):
        current = self.soln
        chain = [current]
        while current.parent != None:
            chain.append(current.parent)
            current = current.parent
        return chain

    def path(self):
        path = [node.operator for noe in self.ancestralChain()[-2::-1]]
        return path

    def bfs(self,state):
        frontier = deque()
        frontier.append(state)
        froxplored = set()
        while frontier:
            board = frontier.popleft()
            froxplored.add((tuple(board.state)))
            if board.goal_test():
                self.soln = board
                self.path = self.path()
                self.nodesExpanded = len(froxplored) - len(frontier) - 1
                return self.soln
            for neighbor in board.neighbors():
                if tuple(neighbor.state) not in froxplored:
                    frontier.append((neighbor))
                    froxplored.add(tuple(neighbor.state))
                    self.maxDepth = max(self.maxDepth , neighbor.depth)
            
        return None

    def dfs(self , state):
        frontier = []
        frontier.append(state)
        froxexplored = set()
        while frontier:
            board = frontier.pop()
            froxexplored.add(tuple(board.state))
            if board.goal_test():
                self.soln = board
                self.path = self.path()
                self.nodesExpanded = len(froxexplored) - len(frontier) - 1
                return self.soln
            for neighbor in board.neighbors()[::-1]:
                if tuple(neighbor.state) not in froxexplored:
                    frontier.append(neighbor)
                    froxexplored.add(tuple(neighbor.state))
                    self.maxDepth = max(self.maxDepth, neighbor.depth)
        
        return None;


    def ast(self, state):
        frontier = []
        heapq.heappush(frontier, state)
        froxexplore = set()

        while frontier:
            board = heapq.heappop(frontier)
            froxexplore.add(tuple(board.state))
			if board.goal_test():
				self.soln = board
				self.path = self.path()
				self.nodes_expanded = len(froxplored)-len(frontier)-1
				return self.soln
			for neighbor in board.neighbors()[::-1]:
				if tuple(neighbor.state) not in froxplored:
					frontier.append(neighbor)
					froxplored.add(tuple(neighbor.state))
					self.max_depth = max(self.max_depth, neighbor.depth)
		return None                

def main():
    p = Board(np.array(eval(sys.argv[2])))
    s  = Solver()

    if sys.argv[1] == 'bfs':
        soln = s.bfs(p)
    elif sys.argv[1] == 'dfs':
        soln = s.dfs(p)
    elif sys.argv[1] == 'ast':
        soln = s.ast(p)

    file = open('output.txt', 'w')

	file.write('path_to_goal: ' + str(s.path) + '\n')
	file.write('cost_of_path: ' + str(len(s.path)) + '\n')
	file.write('nodes_expanded: ' + str(s.nodes_expanded) + '\n')
	file.write('search_depth: ' + str(soln.depth) + '\n')
	file.write('max_search_depth: ' + str(s.max_depth) + '\n')
	file.write('running_time: ' + str(resource.getrusage(resource.RUSAGE_SELF).ru_utime + \
							resource.getrusage(resource.RUSAGE_SELF).ru_stime) + '\n')
	file.write('max_ram_usage: ' + str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024))

	file.close()

if __name__ == "__main__":
	main()
