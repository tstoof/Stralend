# course: Project Computational Science, University of Amsterdam
# authors: Tamara Stoof, Emma Kok, Esmée van der Mark
# group: Stralend
# date: 26-01-2021

# this file contains the cellular automata 
# that simulates a forest fire in Dumai



                    #### IMPORT MODULES AND DEFINE FUNCTIONS ####


import matplotlib.pyplot as plt 
import numpy as np
import math
import json
from matplotlib import colors


def burning_probability(theta, V, c1, c2, Ph, Pden, Pveg):
    """
        This function calculates the probability of a cell
        to catch fire (go to burning state) based on the Pveg and Pden
        of the cell as well as the location of the neighbouring cell relative 
        to the cell and the north. The location of the neighbour cell impacts the
        burning probability of the cell due to wind speed and direction
        Input:
            theta:  int - angle based on position of neighbouring cell
            V:      int - wind speed
            c1:     float - wind constant
            c2:     float - float constant
            Ph:     float - constant probability that a cell adjacent to a burning cell 
                            containing a given type of vegetation and density
                            will catch fire at the next time step under no wind and flat terrain conditions
            Pden:   float - type of vegetation in the cell
            Pveg:   float - density of the vegetation in the cell
        Output:
            Pburn: float -  the probability that a cell adjecent to a burning cell will 
                            catch fire in the next time step
    """
    # compute wind effects
    ft = math.e**(V*c2*(math.cos(theta)-1))
    Pw = ft*math.e**(c1*V)

    # compute burning probability
    Pburn = Ph*(1+Pden)*(1+Pveg)*Pw
    
    return Pburn



                        #### MAIN PROGRAM #### 
"""
    Overview of the different possible states of a cell:
    0	Water		
    1	Fuel	Sparse	Agricultural (-0.3)
    2	Fuel	Sparse	Thickets (0)
    3	Fuel	Sparse	Hallepo-pine (0.4)
    4	Fuel	Normal	Agricultural (-0.3)
    5	Fuel	Normal	Thickets - hele lichte bruin (0)
    6	Fuel	Normal	Hallepo-pine  (0.4)
    7	Fuel	Dense	Agricultural (-0.3)
    8	Fuel	Dense 	Thickets (0)
    9	Fuel	Dense	Hallepo-pine (0.4)
    10 Burning		
    11 Burnt		
    12 city
    13 fireline
"""

# load the grid 
with open("grid.txt") as f:
    grid = json.load(f)

# set fire 
grid[68][39] = 10
grid[68][40] = 10

# model parameters
rows = len(grid)
cols = len(grid[0])

# find total amount of vegetation in grid 
# for fraction calculation
total_vegetation = 0
for row in range(rows):
    for col in range(cols):
        
        # if gridcel not vegetation increase counter
        if grid[row][col] != 0:
            total_vegetation += 1


# create a gridline with only zeros
gridline = []
for row in range(cols):
    gridline.append(0)

# use gridline to make a grid of only zeros
timeBurning = []
for col in range(rows):
    timeBurning.append(list(gridline))


# initialize lists 
row_list = []
col_list = []
list_original_values = []

# choose to use fire line or not 
# (used only for filename creation):
# 0 = fire lines on
# 1 = fire lines off
noFireLines = 1

# choose fire line:
# 0 = no fire lines
# 1 = temporary fireline 
# 2 = the constructed fireline 
typeOfFireline = 1

# choose distance of temporay fire line:
# 1 = directly on the fire propagation front
# 2 = behind the propagation front
# 3 = at a distance ahead of the fire
# propagation front
distanceTemporaryFireline = 3

# choose distance of constructed fire lines:
# 1 = 1.25 km
# 2 = 2.50 km
# 3 = 3.75 km
distanceConstructedFireline = 3

# choose shape of constructed fire lines:
# 1 = triangle 
# 2 = square 
# 3 = straight line 
shapeConstructedFireline = 3

# variable to keep track of the length of the fire line 
lengthFireline = 0

# constants in calculation Pburn
Ph = 0.58 # s/m
c1 = 0.045 # s/m
c2 = 0.131 # s/m
V = 8 # m/s

# model parameters
# set repeats to 1 for visualisation of simulation
repeats = 1
time = 14

# choose to write/append data to txt file or not
# 0 = does not write/append data
# 1 = writes/appends data
write_to_file = 0

# lists for statistics
burning_list = []
burnt_list = []
fuel_list = []

# run simulation n times
for repeat in range(repeats):
    
    # load original grid cell for every 
    # new simulation
    with open("grid.txt") as f:
        grid = json.load(f)

    # set fire 
    grid[68][39] = 10
    grid[68][40] = 10
    grid[0][0] = 13
    
    # simulation has a length of t days
    for t in range(time):
        
        # reset statistics counter
        burnt = 0

        # if temporary fire lines are on then 
        # initialize temporary fire lines on 5th day
        if t == 5 and typeOfFireline == 1:
            
            # loop through every cell in grid except boundaries
            for row in range(1,rows - 1):
                for col in range(1, cols - 1):
                    
                    # checking where burning fire front is (state 10)
                    if grid[row][col] == 10:
                        
                        # save location of front
                        row_list.append(row)
                        col_list.append(col)

            # checking if there is a fire front 
            if len(row_list) > 0 and len(col_list) > 0:
                
                # smallest value of row_list is the
                # most Northern place of the fire front
                smallest_row = min(row_list)
            
                # width of fire front is the minimum and 
                # the maximum of col_list
                smallest_width = min(col_list)
                highest_width = max(col_list)

                # create temporary fire line at distance 1
                if distanceTemporaryFireline == 1:
                    
                    # specify location of fire line in range loop
                    for row in range(smallest_row, smallest_row + 1):
                        for col in range(smallest_width - 2, highest_width + 3 ):
                            
                            # list to store the original states of cells  
                            list_original_values.append(grid[row][col])
                            
                            # change state of cell to fire line state (13)
                            grid[row][col] = 13

                            # increase length fire line
                            lengthFireline = lengthFireline + 1

                # create temporary fire line at distance 2
                if distanceTemporaryFireline == 2:

                    # specify location of fire line in range loop
                    for row in range(smallest_row+2, smallest_row + 3):
                        for col in range(smallest_width-2, highest_width + 3 ):
                            
                            # list to store the original states of cells 
                            list_original_values.append(grid[row][col])
                            
                            # change state of cell to fire line state (13)
                            grid[row][col] = 13
                
                            # increase length fire line
                            lengthFireline = lengthFireline + 1

                # create temporary fire line at distance 3
                if distanceTemporaryFireline == 3:

                    # specify location of fire line in range loop
                    for row in range(smallest_row -5, smallest_row -4):
                        for col in range(smallest_width - 2, highest_width + 3 ):

                            # list to store the original states of cells 
                            list_original_values.append(grid[row][col])
                            
                            # change state of cell to fire line state (13)
                            grid[row][col] = 13

                            # increase length fire line
                            lengthFireline = lengthFireline + 1
        
        # x keeps track of index for the following for-loop
        x = 0
        
        # at time step 8 return cells of temporary fire
        # line at distance 1 to their original state
        if t == 8 and typeOfFireline == 1 and distanceTemporaryFireline == 1 and lengthFireline > 0:
            
            for col in range(smallest_width - 2, highest_width + 3):
                
                # return cells to their original state 
                grid[smallest_row][col] = list_original_values[x]

                # if original state was burning state (10)
                # set new state to burnt (11)
                if list_original_values[x] == 10:
                    grid[smallest_row][col] = 11

                # keep track of index of 
                # list_original_values list
                x = x + 1

        # at time step 8 return cells of temporary fire
        # line at distance 2 to their original state
        if t == 8 and typeOfFireline == 1 and distanceTemporaryFireline == 2 and lengthFireline > 0:
            for col in range(smallest_width - 2, highest_width + 3):
                
                # return cells to their original state 
                grid[smallest_row+2][col] = list_original_values[x]

                # if original state was burning state (10)
                # set new state to burnt (11)
                if list_original_values[x] == 10:
                    grid[smallest_row+2][col] = 11

                # keep track of index of 
                # list_original_values list
                x = x + 1

        # at time step 8 return cells of temporary fire
        # line at distance 3 to their original state
        if t == 8 and typeOfFireline == 1 and distanceTemporaryFireline == 3 and lengthFireline > 0:
            for col in range(smallest_width - 2, highest_width + 3):
                
                # return cells to their original state 
                grid[smallest_row-5][col] = list_original_values[x]

                # if original state was burning state (10)
                # set new state to burnt (11)
                if list_original_values[x] == 10:
                    grid[smallest_row-5][col] = 11

                # keep track of index of 
                # list_original_values list
                x = x + 1

        # if constructed firelines are on then
        # initialize constructed fire lines on day 6th
        if t == 6 and typeOfFireline == 2:
            
            # loop through every cell in grid except boundaries
            for row in range(1,rows - 1):
                for col in range(1, cols - 1):
                    
                    # check where bruning fire front (state 10) is 
                    if grid[row][col] == 10:

                        # construct fireline of shape 1
                        if shapeConstructedFireline == 1:

                            # construct fireline at distance '1'
                            if distanceConstructedFireline == 1:

                                # set chosen gridcells to fire line state
                                grid[row-2][col] = 13
                                grid[row-2][col-1] = 13
                                grid[row-2][col+1] = 13
                                grid[row-2][col-2] = 13
                                grid[row-2][col+2] = 13
                                grid[row-1][col+2] = 13
                                grid[row-1][col-2] = 13
                                grid[row-1][col-3] = 13
                                grid[row-1][col+3] = 13
                                grid[row][col-3] = 13
                                grid[row][col+3] = 13

                            # construct fireline at distance '2'
                            if distanceConstructedFireline == 2:

                                # set chosen gridcells to fire line state
                                grid[row-3][col] = 13
                                grid[row-3][col-1] = 13
                                grid[row-3][col+1] = 13
                                grid[row-3][col-2] = 13
                                grid[row-3][col+2] = 13
                                grid[row-2][col+2] = 13
                                grid[row-2][col-1] = 13
                                grid[row-2][col-3] = 13
                                grid[row-2][col+3] = 13
                                grid[row-1][col-3] = 13
                                grid[row-1][col+3] = 13

                            # constructing the fireline at distance '3'
                            if distanceConstructedFireline == 3:

                                # set chosen gridcells to fire line state
                                grid[row-4][col] = 13
                                grid[row-4][col-1] = 13
                                grid[row-4][col+1] = 13
                                grid[row-4][col-2] = 13
                                grid[row-4][col+2] = 13
                                grid[row-3][col+2] = 13
                                grid[row-3][col-2] = 13
                                grid[row-3][col-3] = 13
                                grid[row-3][col+3] = 13
                                grid[row-2][col-3] = 13
                                grid[row-2][col+3] = 13
                                
                        # construct fire line of shape 2        
                        if shapeConstructedFireline == 2:
                            
                            # constructing the fireline at distance '1'
                            if distanceConstructedFireline == 1:

                                # set chosen gridcells to fire line state
                                grid[row-2][col] = 13
                                grid[row-2][col-1] = 13
                                grid[row-2][col+1] = 13
                                grid[row-2][col+2] = 13
                                grid[row-2][col-2] = 13
                                grid[row-1][col-2] = 13
                                grid[row-1][col+2] = 13

                            # constructing the fireline at distance '2'
                            if distanceConstructedFireline == 2:

                                # set chosen gridcells to fire line state
                                grid[row-3][col] = 13
                                grid[row-3][col-1] = 13
                                grid[row-3][col+1] = 13
                                grid[row-3][col+2] = 13
                                grid[row-3][col-2] = 13
                                grid[row-2][col-2] = 13
                                grid[row-2][col+2] = 13

                            # constructing the fireline at distance '3'
                            if distanceConstructedFireline == 3:

                                # set chosen gridcells to fire line state
                                grid[row-4][col] = 13
                                grid[row-4][col-1] = 13
                                grid[row-4][col+1] = 13
                                grid[row-4][col+2] = 13
                                grid[row-4][col-2] = 13
                                grid[row-3][col-2] = 13
                                grid[row-3][col+2] = 13

                        # construct fire line of shape 3
                        if shapeConstructedFireline == 3:

                            # constructing the fireline at distance '3'
                            if distanceConstructedFireline == 1:

                                # set chosen gridcells to fire line state
                                grid[row-2][col] = 13
                                grid[row-2][col-1] = 13
                                grid[row-2][col+1] = 13

                            # constructing the fireline at distance '3'
                            if distanceConstructedFireline == 2:

                                # set chosen gridcells to fire line state
                                grid[row-3][col] = 13
                                grid[row-3][col-1] = 13
                                grid[row-3][col+1] = 13

                            # constructing the fireline at distance '3'
                            if distanceConstructedFireline == 3:

                                # set chosen gridcells to fire line state
                                grid[row-4][col] = 13
                                grid[row-4][col-1] = 13
                                grid[row-4][col+1] = 13

        # loop through every gridcell except at the boundaries
        for row in range(1,rows-1):
            for col in range(1,cols-1):

                # keep track of how long a cell has been burning
                if grid[row][col] == 10:
                    timeBurning[row][col] += 1

                # allocate Pden and Pveg values depending 
                # on state of cell (see state list above)

                # sparse vegetation
                if grid[row][col] == 1:
                    Pden = -0.4
                    Pveg = -0.3
                elif grid[row][col] == 2:
                    Pden = -0.4
                    Pveg = 0
                elif grid[row][col] == 3:
                    Pden = -0.4
                    Pveg = 0.4
                
                # normal vegetation
                elif grid[row][col] == 4:
                    Pden = 0
                    Pveg = -0.3
                elif grid[row][col] == 5:
                    Pden = 0
                    Pveg = 0
                elif grid[row][col] == 6:
                    Pden = 0
                    Pveg = 0.4

                # dense vegetation
                elif grid[row][col] == 7:
                    Pden = 0.3
                    Pveg = -0.3
                elif grid[row][col] == 8:
                    Pden = 0.3
                    Pveg = 0
                elif grid[row][col] == 9:
                    Pden = 0.3
                    Pveg = 0.4
                

                # compute Pburn for burning neighbour cells
                # using the a Moore neighborhood (8 neighbours)
                # and the location/angle (theta) of neighbour cell
                # relative to cell and the North
                if grid[row+1][col-1] == 10:
                    theta = 45
                    Pburn_1 = burning_probability(theta, V, c2, c1, Ph, Pden, Pveg) 

                if grid[row+1][col+1] == 10:
                    theta = 45      
                    Pburn_2 = burning_probability(theta, V, c2, c1, Ph, Pden, Pveg)
                    
                if grid[row+1][col] == 10:
                    theta = 0
                    Pburn_3 = burning_probability(theta, V, c2, c1, Ph, Pden, Pveg)

                if grid[row][col-1] == 10:
                    theta = 90
                    Pburn_4 = burning_probability(theta, V, c2, c1, Ph, Pden, Pveg)
                    
                if grid[row][col+1] == 10:          
                    theta = 90
                    Pburn_5 = burning_probability(theta, V, c2, c1, Ph, Pden, Pveg)
                
                if grid[row-1][col-1] == 10:                   
                    theta = 135
                    Pburn_6 = burning_probability(theta, V, c2, c1, Ph, Pden, Pveg)

                if grid[row-1][col+1] == 10:
                    theta = 135
                    Pburn_7 = burning_probability(theta, V, c2, c1, Ph, Pden, Pveg)

                if grid[row-1][col] == 10:
                    theta = 180
                    Pburn_8 = burning_probability(theta, V, c2, c1, Ph, Pden, Pveg)


                # Pburn = 0 if neighbour is not burning
                if grid[row+1][col-1] != 10:
                    Pburn_1 = 0 

                if grid[row+1][col+1] !=  10:
                    Pburn_2 = 0
                    
                if grid[row+1][col] != 10:
                    Pburn_3 = 0

                if grid[row][col-1] != 10:
                    Pburn_4 = 0
                    
                if grid[row][col+1] != 10:
                    Pburn_5 = 0
                
                if grid[row-1][col-1] != 10:
                    Pburn_6 = 0

                if grid[row-1][col+1] != 10:
                    Pburn_7 = 0

                if grid[row-1][col] != 10:
                    Pburn_8 = 0

            
                # compute chance of current cell catching fire
                # cell can only catch fire if state is 1-9
                # chance of neighbour setting cell on fire
                # is independent of other neighbour cells
                if (grid[row][col] != 0 and  grid[row][col] != 10 and grid[row][col] != 11 and grid[row][col] != 13) and \
                    (np.random.uniform() < Pburn_1 or np.random.uniform() < Pburn_2 or np.random.uniform() < Pburn_3 or\
                    np.random.uniform() < Pburn_4 or np.random.uniform() < Pburn_5 or np.random.uniform() < Pburn_6 or \
                    np.random.uniform() < Pburn_7 or np.random.uniform() < Pburn_8):
                    
                        # set cell to burning
                        grid[row][col] = 10   
                        
                        # start count of number of time steps 
                        # cell is burning
                        timeBurning[row][col] += 1                                        

                # after 2 timesteps (and if cell is not a fireline (13))
                # turn burning state (10) to burnt state (11)
                if timeBurning[row][col] == 2 and grid[row][col] != 13:
                    grid[row][col] = 11

                # keep track of number of burnt cells for statistics
                if grid[row][col] == 11:
                    burnt += 1

        # create visualisation of simulation
        if repeats == 1:

            # create barplot once
            if t == 0:

                # specify colorbar characteristics
                cmap = colors.ListedColormap(['aqua', 'goldenrod', 'gold', 'yellow', 'greenyellow', 'lawngreen', 'olivedrab', 'green', 'limegreen', 'darkgreen', 'orangered', 'red', 'dimgray', 'brown'])
                colormap = plt.imshow(grid, cmap= cmap)
                cbar = plt.colorbar(colormap)
                cbar.set_ticks([0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
                cbar.set_ticklabels(["Water", "Fuel (Sparse/-0.3)", "Fuel (Sparse/0)", "Fuel (Sparse/0.4)", "Fuel (Normal/-0.3)", "Fuel (Normal/0)", 
                                    "Fuel(Normal/0.4)", "Fuel (Dense/-0.3)", "Fuel (Dense/0)", "Fuel (Dense/0.4)", "Burning", "Burnt", "City", "Fire lines"])
        
            # draw grid for every time step
            plt.imshow(grid, cmap=cmap)    
            plt.draw()
            plt.pause(0.2)
        
    # statistics 
    # 50 times the end state of fraction burnt cells
    burnt_list.append(burnt/total_vegetation)

    
    # filenames for storing data
    if noFireLines == 0:
 
        if typeOfFireline == 1 and distanceTemporaryFireline == 1:
            filename = "temporary_distance_1"

        if typeOfFireline == 1 and distanceTemporaryFireline == 2:
            filename = "temporary_distance_2"

        if typeOfFireline == 1 and distanceTemporaryFireline == 3:
            filename = "temporary_distance_3"

        if typeOfFireline == 2 and distanceConstructedFireline == 1 and shapeConstructedFireline == 1:
            filename = "constructed_distance_1_shape_1"

        if typeOfFireline == 2 and distanceConstructedFireline == 1 and shapeConstructedFireline == 2:
            filename = "constructed_distance_1_shape_2"

        if typeOfFireline == 2 and distanceConstructedFireline == 1 and shapeConstructedFireline == 3:
            filename = "constructed_distance_1_shape_3"

        if typeOfFireline == 2 and distanceConstructedFireline == 2 and shapeConstructedFireline == 1:
            filename = "constructed_distance_2_shape_1"

        if typeOfFireline == 2 and distanceConstructedFireline == 2 and shapeConstructedFireline == 2:
            filename = "constructed_distance_2_shape_2"

        if typeOfFireline == 2 and distanceConstructedFireline == 2 and shapeConstructedFireline == 3:
            filename = "constructed_distance_2_shape_3"

        if typeOfFireline == 2 and distanceConstructedFireline == 3 and shapeConstructedFireline == 1:
            filename = "constructed_distance_3_shape_1"
            
        if typeOfFireline == 2 and distanceConstructedFireline == 3 and shapeConstructedFireline == 2:    
            filename = "constructed_distance_3_shape_2"

        if typeOfFireline == 2 and distanceConstructedFireline == 3 and shapeConstructedFireline == 3:          
            filename = "constructed_distance_3_shape_3"        

    if noFireLines == 1:
        filename = "noFireLines"

# only use if you want to change the data files
# and append new data values to file
if write_to_file == 1:
    with open(filename + ".txt", 'a') as f:
        
        # append fraction burnt data to file
        f.write(str(burnt_list)+"\n")

# create visual final result of simulation
if repeats == 1:

    # specify colorbar characteristics
    plt.figure()
    cmap = colors.ListedColormap(['aqua', 'goldenrod', 'gold', 'yellow', 'greenyellow', 'lawngreen', 'olivedrab', 'green', 'limegreen', 'darkgreen', 'orangered', 'red', 'dimgray', 'brown'])
    colormap = plt.imshow(grid, cmap= cmap)
    cbar = plt.colorbar(colormap)
    cbar.set_ticks([0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
    cbar.set_ticklabels(["Water", "Fuel (Sparse/-0.3)", "Fuel (Sparse/0)", "Fuel (Sparse/0.4)", "Fuel (Normal/-0.3)", "Fuel (Normal/0)", 
                        "Fuel(Normal/0.4)", "Fuel (Dense/-0.3)", "Fuel (Dense/0)", "Fuel (Dense/0.4)", "Burning", "Burnt", "City", "Fire lines"])
    plt.show()