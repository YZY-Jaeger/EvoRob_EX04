import numpy as np
import math

class Evolution():
    @staticmethod
    def calculate_fitness(agent, grid_size=10):
        # Get the current position of the agent
        x, y, _ = agent.get_position()

        # Check if the agent is within the 500x500 grid
        if not (0 <= x <= 500 and 0 <= y <= 500):
            return -1
        
        # Calculate the grid cell that the agent is currently in
        grid_x = int(x / grid_size)
        grid_y = int(y / grid_size)
        #print(grid_x,grid_y)
        # Add the current grid cell to the set of visited cells
        agent.visited_grid_cells.add((grid_x, grid_y))

        # The fitness is the number of unique grid cells visited
        fitness = len(agent.visited_grid_cells)

        return fitness