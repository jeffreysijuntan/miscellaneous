#Created by Jeffrey Tan
import random
import copy

def maze_generator():
	maze = [i for i in range(9)]
	random.shuffle(maze);
	return tuple(maze)

def is_goal(maze):
	for i in range(8):
		if maze[i] != i+1:
			return False
	return True

def solve(*args):
	maze = tuple(args)
	initial_state = State(maze)
	if (is_goal(maze)): 
		return initial_state
	frontier = MyPriorityQueue()
	frontier.put(initial_state, initial_state.heuristic())
	visited = set()
	visited.add(initial_state.maze)
	while frontier.qsize() > 0:
		print(frontier.qsize())
		curr_state = frontier.get()
		new_states = next_states(curr_state)
		for next_state in new_states:
			if next_state.maze not in visited:
				if (is_goal(next_state.maze)):
					return next_state;
				visited.add(next_state.maze)
				frontier.put(next_state, next_state.heuristic())
		
	return 'unsolvable'

def next_states(state):
	states = [] #list of neighbor states
	for idx, num in enumerate(state.maze):
		if num is 0:
			x, y = idx // 3, idx % 3
			neighbors = [[x-1,y], [x,y-1], [x+1,y], [x,y+1]]
			neighbors = [(i,j) for i,j in neighbors if (0<= i<3 and 0<=j<3)] #delete those outside boundary neighbors
			for i, j in neighbors:
				new_maze = list(state.maze)
				new_maze[idx] = new_maze[i*3+j]
				new_maze[i*3+j] = 0
				new_state = State(tuple(new_maze), 1+state.steps, state)
				states.append(new_state)
	return states

def show_path(state):
	if isinstance(state, str):
		print(state)
		return
	path = []
	while state.parent is not None:
		path.append(state.maze)
		state = state.parent
	path.append(state.maze)
	print('number of moves: ' + str(len(path) - 1))
	print(path[::-1])


def test():
	goal = [1,2,3,4,8,5,7,0,6]
	goal2 = [1,2,3,4,0,5,7,8,6]
	maze1 = [(4, 2, 7, 8, 3, 1, 6, 0, 5), 17]
	maze2 = [8,6,7,2,5,4,3,0,1]
	maze3 = [6,4,7,8,5,0,3,2,1]
	random_maze = maze_generator()
	goal_state = solve(*maze3)
	show_path(goal_state)

class State():
	def __init__(self, maze, steps=0, parent=None):
		self.maze = maze
		self.steps = steps
		self.parent = parent

	def __eq__(self, other):
	    if isinstance(self, other.__class__):
	        return self.maze == other.maze
	    return False

	def heuristic(self):
		return self.manhattan() + self.step_penalty()

	def manhattan(self):
		dist = 0
		for idx, num in enumerate(self.maze):
			if num is not 0:
				target_x = (num-1) // 3
				target_y = (num-1) % 3
				x = idx // 3
				y = idx % 3
				dist += abs(x-target_x) + abs(y-target_y)
		return dist

	def step_penalty(self):
		return self.steps

	def is_unique(self):
		curr_state = self
		while curr_state.parent is not None:
			curr_state = curr_state.parent
			if self == curr_state:
				return False
		return True


from queue import PriorityQueue

class  MyPriorityQueue(PriorityQueue):
    def __init__(self):
        PriorityQueue.__init__(self)
        self.counter = 0

    def put(self, item, priority):
        PriorityQueue.put(self, (priority, self.counter, item))
        self.counter += 1

    def get(self, *args, **kwargs):
        _, _, item = PriorityQueue.get(self, *args, **kwargs)
        return item

if __name__ == '__main__':
	test()