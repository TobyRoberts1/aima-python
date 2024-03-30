from time import time
from search import *
from assignment1aux import *

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
                        if row == 0 :
                            list_actions.append(((row,col), 'down'))
                        #checks the bottom row and that it is empty
                        if row == height -1 :
                            list_actions.append(((row,col), 'up'))
                        
                        #checks the right column and that it is empty
                        if col == width - 1 :
                            list_actions.append(((row,col), 'left'))
                        #checks the left column and that it is empty
                        if col == 0 :
                            list_actions.append(((row,col), 'right'))

        #this only runs if he has hit a rock or raked tile, when he is in the garden.       
        else:   
                 
            row, col = monk_pos
            #checks if it is facing left or right so it can only move up or down. 
            if monk_dir == 'left' or monk_dir == 'right':
                #check if monk can move up
                if row > 0 and garden[row][col] == '':
                    list_actions.append(((row,col), 'up'))
                #check if monk can move down
                if row <= height and garden[row][col] == '':
                    list_actions.append(((row,col), 'down'))
            elif monk_dir == 'up' or monk_dir == 'down':

                #check if monk can move left
                if col >= 0 and garden[row][col] == '':
                    list_actions.append(((row,col), 'left'))
                #check if monk can move right 
                if col <= width  and garden[row][col] == '':
                    list_actions.append(((row,col), 'right'))
                            

                            
        # print(list_actions)
        # print("\n")
        
        return list_actions
    
        
        
    def result(self, state, action):
    # Task 2.2
    # Return a new state resulting from a given action being applied to a given state.
        garden = state[0]
        monk_pos = state[1]
        monk_dir = state[2]
        
        #print(state)
        garden = [list(row) for row in garden]
        

        if monk_pos is None:
                # If monk is not in the garden, update its position and direction to be in the garden 
                monk_pos = action[0]
                monk_dir = action[1]

        new_row, new_col = monk_pos
        while True: 
            
            #else: 
                #loops through untill it goes outside the garden, hits a rock, hits a raked tile. 
                # If monk is already in the garden, simulate its movement based on the action
                
                
                direction = action[1]

                # Check if the new position is within the garden boundaries
                if 0 <= new_row < len(garden) and 0 <= new_col < len(garden[0]):
                   
                     # Check if the new position is a valid move (not a rock or raked tile)
                    if garden[new_row][new_col] == '':
                        
                        monk_pos = (new_row, new_col)
                        monk_dir = direction
                        

                    # Update monk's position based on the direction
                        if direction == 'up':
                            if new_row != len(garden) - 1:
                                #CANT USE THE MINUS ONE TO ADD THE THING BEHIND HIM AS ELSE OVER RIGHTS IT WHEN IT IS IN THE MAP
                                #THAT IS WHY WHEN RUNS IT IS CUTS THE MAP IN HALF AND CHANGES THE ARROWS BEHIND IT. 



















                                garden[new_row + 1][new_col] = direction
                            new_row -= 1
                            
                        elif direction == 'down':
                            if new_row != 0:
                                garden[new_row - 1][new_col] = direction
                            new_row += 1
                            
                        elif direction == 'left':
                            if new_col != len(garden[0]) - 1:
                                garden[new_row][new_col + 1] = direction
                            new_col -= 1
                            
                        elif direction == 'right':
                            if new_col != 0:
                                garden[new_row][new_col - 1] = direction
                            new_col += 1
                            

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
astar_heuristic_cost = None

def beam_search(problem, f, beam_width):
    # Task 4
    # Implement a beam-width version A* search.
    # Return a search node containing a solved state.
    # Experiment with the beam width in the test code to find a solution.
    # Replace the line below with your code.
    raise NotImplementedError

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
    '''
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
    '''

    # Task 4 test code
    '''
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
    '''














































































































        







'''
    def result(self, state, action):
        # Task 2.2
        # Return a new state resulting from a given action being applied to a given state.
        garden = state[0]
        monk_pos = state[1]
        monk_dir = state[2]
        #new_garden = [list(row) for row in garden]  # Make a deep copy of the garden

        if monk_pos is None: 
            monk_pos = action[0]
            monk_dir = action[1]
            garden[monk_pos[0]][monk_pos[1]] = monk_dir #sets the position that the monk entered to the direction the monk is going

        while monk_dir == 'up':
            #move up untill off garden or hits rock or raked tile
            monk_pos[1] = monk_pos[1] + 1
            garden[monk_pos[0]][monk_pos[1]] = monk_dir
            if monk_pos == None:
                break
            if monk_pos == 'rock' or 'up' or 'down' or 'left' or 'right': 
                monk_pos[1] = monk_pos[1] -1
                break

        while monk_dir == 'down':
            #move down untill off garden or hits rock or raked tile
            monk_pos[1] = monk_pos[1] - 1
            garden[monk_pos[0]][monk_pos[1]] = monk_dir
            if monk_pos == None:
                break
            if monk_pos == 'rock' or 'up' or 'down' or 'left' or 'right': 
                monk_pos[1] = monk_pos[1] + 1
                break
        
        while monk_dir == 'left':
            #move right untill off garden or hits rock or raked tile
            monk_pos[1] = monk_pos[1] - 1
            garden[monk_pos[0]][monk_pos[1]] = monk_dir
            if monk_pos == None:
                break
            if monk_pos == 'rock' or 'up' or 'down' or 'left' or 'right': 
                monk_pos[1] = monk_pos[1] + 1
                break

        while monk_dir == 'right':
            #move right untill off garden or hits rock or raked tile
            monk_pos[1] = monk_pos[1] + 1
            garden[monk_pos[0]][monk_pos[1]] = monk_dir
            if monk_pos == None:
                break
            if monk_pos == 'rock' or 'up' or 'down' or 'left' or 'right': 
                monk_pos[1] = monk_pos[1] - 1
                break
'''

        
            # if monk_pos is None:  # Monk is not in the garden, entering from the perimeter
            #     new_pos, new_dir = action
            #     new_garden[new_pos[0]][new_pos[1]] = new_dir # Mark the entered tile as raked
            #     return (new_garden, new_pos, new_dir)
            # else:  # Monk is already in the garden
            #     new_position, new_direction = action
            #     new_row, new_col = new_position

            #     if new_garden[new_row][new_col] == '':
            #         # Mark the previous position as raked
            #         new_garden[monk_position[0]][monk_position[1]] = 'raked'

            #         # Move the monk to the new position
            #         new_garden[new_row][new_col] = 'T'

            #         return (new_garden, new_position, new_direction)
            #     else:
            #         return state  # Monk can't move to the new position (rock or raked), return the same state




    






        # # garden, monk_position, monk_direpathction = state
        # # height = len(garden)'rock'
        # # width = len(garden[0])

        # # # Check if all unraked tiles have been raked
        # # for row in range(height):
        # #      # Check if there are any unraked tiles left in the garden
        # if any('' in row for row in garden):
        #     return False # There are still unraked tiles, so the goal is not satisfied
            
        # # Check if the monk has returned to the perimeter of the garden
        # if monk_position is not None:
        #     row, col = monk_position
        #     height, width = len(garden), len(garden[0])
        #     if row == 0 or row == height - 1 or col == 0 or col == width - 1:
        #         return True # Monk is back at the perimeter, goal is satisfied
        
        #     return False # Monk is not back at the perimeter, goal is not satisfied   for col in range(width):
        # #         if garden[row][col] == '':
        # #             return False  # Unraked tile found, goal not reached

        # # # Check if the monk is back at the perimeter
        # # if monk_position is not None:
        # #     row, col = monk_position
        # #     if row == 0 or row == height - 1 or col == 0 or col == width - 1:
        # #         return True  # Monk is back at the perimeter, goal reached
        # # return False  # Monk is not back at the perimeter, goal not reached
    
































# from time import time
# from search import *
# from assignment1aux import *

# def read_initial_state_from_file(filename):
#     # Task 1
#     # Return an initial state constructed using a configuration in a file.
#     # Replace the line below with your code.
    
#     with open(filename, 'r') as file:
#         #read lines of the file
#         height = int(file.readline())
#         width = int(file.readline())

#         #creates an empty garden 
#         garden = [[''] * width for _ in range(height)]

#         #find rock postions and makes them. pointer currently at line 3. 
#         for line in file: 
#             postion = line.strip().split(',')
#             row = int (postion[0])
#             col = int (postion[1])
#             garden[row][col] = 'rock'
        
#         monk_pos = None
#         Monk_dir = None
#         #converts garden and everything else to a tuple
#         state = (tuple(tuple(tile)for tile in garden), monk_pos, Monk_dir)
#         print(state)

#     return state

# class ZenPuzzleGarden(Problem):
#     def __init__(self, initial):
#         if type(initial) is str:
#             super().__init__(read_initial_state_from_file(initial))
#         else:
#             super().__init__(initial)

#      # Return a list of all allowed actions in a given state.
#     def actions(self, state):
#         # Task 2.1
#         # Replace the line below with your code.
#         monk_pos = state[1]
#         monk_dir = state[2]
#         list_actions = []

#         #checks where the monk can enter from when he is outside the garden. 
#         if monk_pos is None: 
#             garden = state[0]
#             height = len(garden)
#             width = len(garden[0])

#             for row in range(height):
#                 for col in range(width):
#                     if garden[row][col] == '':
#                         #checks the top row and that it is empty
#                         if row == 0 and garden[row + 1][col] == '':
#                             list_actions.append(((row,col), 'down'))
#                         #checks the bottom row and that it is empty
#                         if row == height -1 and garden[row - 1][col] == '':
#                             list_actions.append(((row,col), 'up'))
#                         #checks the left column and that it is empty
#                         if col == 0 and garden [row][col - 1] == '':
#                             list_actions.append(((row,col), 'right'))
#                         #checks the right column and that it is empty
#                         if col == width - 1 and garden[row][col - 1] == '':
#                             list_actions.append(((row,col), 'left'))

#         else:
#             garden = state[0]
#             height = len(garden)
#             width = len(garden[0])
#             row, col = monk_pos

#             #checks if it is facing left or right so it can only move up or down. 
#             if monk_dir == 'left' or monk_dir == 'right':
#                 #check if monk can move up
#                 if row > 0 and garden[row - 1][col] == '':
#                     list_actions.append(((row - 1,col), 'up'))
#                 #check if monk can move down
#                 if row < height - 1 and garden[row + 1][col] == '':
#                     list_actions.append(((row + 1,col), 'down'))
#             elif monk_dir == 'up' or monk_dir == 'down':

#                 #check if monk can move left
#                 if col > 0 and garden[row][col - 1] == '':
#                     list_actions.append(((row,col - 1), 'left'))
#                 #check if monk can move right 
#                 if col < width - 1 and garden[row][col +1] == '':
#                     list_actions.append(((row,col + 1), 'right'))
#         return list_actions
        
        

#     def result(self, state, action):
#         # Task 2.2
#         # Return a new state resulting from a given action being applied to a given state.




#         raise NotImplementedError

#     def goal_test(self, state):
#         # Task 2.3
#         # Return a boolean value indicating if a given state is solved.
#         # Replace the line below with your code.
#         raise NotImplementedError

# # Task 3
# # Implement an A* heuristic cost function and assign it to the variable below.
# astar_heuristic_cost = None

# def beam_search(problem, f, beam_width):
#     # Task 4
#     # Implement a beam-width version A* search.
#     # Return a search node containing a solved state.
#     # Experiment with the beam width in the test code to find a solution.
#     # Replace the line below with your code.
#     raise NotImplementedError

# if __name__ == "__main__":

#     # Task 1 test code
    
#     print('The loaded initial state is visualised below.')
#     visualise(read_initial_state_from_file('assignment1config.txt'))
    
    








    # Task 2 test cod
'''
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
'''

    # Task 3 test code
'''
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
    '''

    # Task 4 test code
'''
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
'''
