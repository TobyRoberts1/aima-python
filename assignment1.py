from time import time
from search import *
from assignment1aux import *
from assignment1 import *


def read_initial_state_from_file(filename):
    # Task 1
    # Return an initial state constructed using a configuration in a file.
    # Replace the line below with your code.
    
    with open(filename, 'r') as file:
        #read lines of the file
        height = int(file.readline())
        width = int(file.readline())

        #creates an empty garden 
        garden = [[''] * width for _ in range(height)]

        #find rock postions and makes them. pointer currently at line 3. 
        for line in file: 
            postion = line.strip().split(',')
            row = int (postion[0])
            col = int (postion[1])
            garden[row][col] = 'rock'
        
        monk_pos = None
        monk_dir = None
        #converts garden and everything else to a tuple
        state = (tuple(tuple(tile)for tile in garden), monk_pos, monk_dir)
        print(state)

    return state

class ZenPuzzleGarden(Problem):
    def __init__(self, initial):
        if type(initial) is str:
            super().__init__(read_initial_state_from_file(initial))
        else:
            super().__init__(initial)

     # Return a list of all allowed actions in a given state.
    def actions(self, state):
        # Task 2.1
        # Replace the line below with your code.
        garden = state[0]
        monk_pos = state[1]
        monk_dir = state[2]
        height = len(garden)
        width = len(garden[0])
        list_actions = []

        #checks where the monk can enter from when he is outside the garden. 
        if monk_pos is None: 
            for row in range(height):
                for col in range(width):
                    if garden[row][col] == '':
                        #checks the top row and that it is empty
                        if row == 0:
                            list_actions.append(((row,col), 'down'))
                        #checks the bottom row and that it is empty
                        if row == height - 1:
                            list_actions.append(((row,col), 'up'))                       
                        #checks the right column and that it is empty
                        if col == width - 1:
                            list_actions.append(((row,col), 'left'))
                        #checks the left column and that it is empty
                        if col == 0:
                            list_actions.append(((row,col), 'right'))

        #this only runs if he has hit a rock or raked tile, when he is in the garden.       
        else:             
            curr_row, curr_col = monk_pos
         
         
            #checks which way monk was facing when hit something so it can turn 90 to see where it can go. 
            if monk_dir == 'left' or monk_dir == 'right':
                #check if monk can move up
                if curr_row - 1 >= 0 and garden[curr_row - 1][curr_col] == '':
                    list_actions.append(((curr_row - 1, curr_col), 'up'))
                
                #check if monk can move down
                if curr_row + 1 <= len(garden) and  garden[curr_row + 1][curr_col] == '':
                    list_actions.append(((curr_row + 1, curr_col), 'down'))

                #checks if the monk can move out of the garden. 
                if curr_row == 0:
                    list_actions.append(((curr_row, curr_col), 'up'))
               
                elif curr_row + 1 == len(garden):
                    list_actions.append(((curr_row, curr_col), 'down'))
                   



            elif monk_dir == 'up' or monk_dir == 'down':
                #check if monk can move left
                if curr_col - 1  >= 0 and garden[curr_row][curr_col - 1] == '':
                    list_actions.append(((curr_row, curr_col - 1), 'left'))

                #check if monk can move right 
                if curr_col + 1 <= len(garden[0]) and garden[curr_row][curr_col + 1] == '':
                    list_actions.append(((curr_row, curr_col + 1), 'right'))

                #checks if the monk can move out of the garden. 
                if curr_col == 0:
                    list_actions.append(((curr_row, curr_col), 'left'))
                    
                elif curr_col + 1 == len(garden[0]):
                    list_actions.append(((curr_row, curr_col), 'right'))
                    

        # print(list_actions)
        # print("\n")
        
        return list_actions
    
        
        
    def result(self, state, action):
    # Task 2.2
    # Return a new state resulting from a given action being applied to a given state.
        garden = state[0]
        monk_pos = state[1]
        monk_dir = state[2]
        
        
        garden = [list(row) for row in garden]
        

        if monk_pos is None:
                # If monk is not in the garden, update its position and direction to be in the garden 
                monk_pos = action[0]
                monk_dir = action[1]

        new_row, new_col = monk_pos
        while True: 
                          
                #move the  
                     
                #loops through untill it goes outside the garden, hits a rock, hits a raked tile. 
                # If monk is already in the garden, simulate its movement based on the action
                
                
                direction = action[1]

                if direction =='up':
                    new_row -= 1
                elif direction == 'down':
                    new_row += 1
                elif direction == 'left':
                    new_col -= 1
                elif direction =='right':
                    new_col += 1

             
                # Check if the new position is within the garden boundaries
                if 0 <= new_row < len(garden) and 0 <= new_col < len(garden[0]):
                   
                     # Check if the new position is a valid move (not a rock or raked tile)
                    if garden[new_row][new_col] == '':
                        
                        monk_pos = (new_row, new_col)
                        monk_dir = direction
                        




                    #can get rid of the following and use the old monk postions and create a new monk pos    
                    # Update monk's position based on the direction
                        if direction == 'up':
                            if new_row != len(garden) - 1:
                                garden[new_row + 1][new_col] = direction
             
                            
                        elif direction == 'down':
                            if new_row != 0:
                                garden[new_row - 1][new_col] = direction
                     
                            
                        elif direction == 'left':
                            if new_col != len(garden[0]) - 1:
                                garden[new_row][new_col + 1] = direction
                            
                            
                        elif direction == 'right':
                            if new_col != 0:
                                garden[new_row][new_col - 1] = direction
                          
                            

                    else: 
                        break 
                else: 
                    monk_dir = None
                    monk_pos = None
                    if direction == 'up':
                        if new_row != len(garden):
                            garden[new_row + 1][new_col] = direction
                        new_row -= 1
                       
                    elif direction == 'down':
                        if new_row != 0:
                            garden[new_row - 1][new_col] = direction
                        new_row += 1
                       
                    elif direction == 'left':
                        if new_col != len(garden[0]):
                            garden[new_row][new_col + 1] = direction
                        new_col -= 1
                       
                    elif direction == 'right':
                        if new_col != 0:
                            garden[new_row][new_col - 1] = direction
                        new_col += 1
                       
                             
                    break


                
        garden= tuple(tuple(row) for row in garden)
        state = (tuple(tuple(tile)for tile in garden), monk_pos, monk_dir)
        state = (garden, monk_pos, monk_dir)
        # print (state)
        # print ('\n')
        # visualise(state)

        return state

    

    def goal_test(self, state):
        #Task 2.3ome/tr272/Documents/COMPX216/aima-python/assignment1.py", line 201, in <module>
        #node = breadth_first_graph_search(garden)

        # Return a boolean value indicating if a given state is solved.
        # Retrieve the relevant information from the state
        garden = state[0]
        monk_pos = state[1]
        monk_dir = state[2]
        i = 0
        #loops through every tile in the garden to check that they have all been raked
        for row in range(len(garden)):
            for col in range(len(garden[0])):
                if garden[row][col] == '':
                    i += 1
        if i == 0 and monk_pos is None and monk_dir is None:
            return True
        else: 
            return False
                
                    
            
     

# Task 3
# Implement an A* heuristic cost function and assign it to the variable below.
def astar_heuristic_cost(node):

    garden, pos, dir = node.state
    height = len(garden)
    width = len(garden[0])
    row_with_empty = 0
    col_with_empty = 0

    # for each row in the garden 
    for row in range (height): 
        #check in each tile
        for tile in range (width) :
            #if there is any emtpy tiles in it. 
            if garden[row][tile] == '':
                row_with_empty += 1
                break
    
    #for each col in the garden 
    for col in range (width): 
        #check in each tile
        for tile in range (height):
            #if there is any emtpy tiles in it. 
            if garden[tile][col] == '':
                col_with_empty += 1
                break
    
    if row_with_empty < col_with_empty:
        return row_with_empty
    else: 
        return col_with_empty

    




def beam_search(problem, f, beam_width):
    # Task 4
    # Implement a beam-width version A* search.
    # Return a search node containing a solved state.
    # Experiment with the beam width in the test code to find a solution.
    # Replace the line below with your code.

    #from breadth-first search 
    f = memoize(f, 'f')
    node = Node(problem.initial)
    frontier = PriorityQueue('min', f)
    frontier.append(node)
    explored = set()
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            
            return node
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                if f(child) < frontier[child]:
                    del frontier[child]
                    frontier.append(child)
        #cut down the frontier to give the best minimum options for the beam search 
        frontier.heap = heapq.nsmallest(beam_width,frontier.heap)

        
    return None








if __name__ == "__main__":

    # Task 1 test code
    
    print('The loaded initial state is visualised below.')
    visualise(read_initial_state_from_file('assignment1config.txt'))


    # Task 2 test code
    
    garden = ZenPuzzleGarden('assignment1config.txt')
    print('Running breadth-first graph search.')
    before_time = time()
    node = breadth_first_graph_search(garden)
    after_time = time()
    print(f'Breadth-first graph search took {after_time - before_time} seconds.')
    if node:
        print(f'Its solution with a cost of {node.path_cost} is animated below.')
        animate(node)
    else:
        print('No solution was found.')
    

    # Task 3 test code
    
    print('Running A* search.')
    before_time = time()
    node = astar_search(garden, astar_heuristic_cost)
    after_time = time()
    print(f'A* search took {after_time - before_time} seconds.')
    if node:
        print(f'Its solution with a cost of {node.path_cost} is animated below.')
        animate(node)
    else:
        print('No solution was found.')
    

    # Task 4 test code
    
    print('Running beam search.')
    before_time = time()
    node = beam_search(garden, lambda n: n.path_cost + astar_heuristic_cost(n), 50)
    after_time = time()
    print(f'Beam search took {after_time - before_time} seconds.')
    if node:
        print(f'Its solution with a cost of {node.path_cost} is animated below.')
        animate(node)
    else:
        print('No solution was found.')
    