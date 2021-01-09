import matplotlib.pyplot as plt 
import numpy as np
import random
import math

# model parameters
rows = 100
cols = 100
time = 100

# create a grid with only zeros
gridline = []
for row in range(rows):
    gridline.append(0)
grid = []
timeBurning = []
for col in range(cols):
    grid.append(list(gridline))
    timeBurning.append(list(gridline))


# randomly assign new states to the cells, leaving the boundaries as zero
for row in range(rows):
    for col in range(cols):
        if row > 2 and row < rows-2 and col>2 and col<cols-2:
            grid[row][col] = random.randint(1,9)


# start a fire in the right bottom corner
grid[row-15][col-15] = 10
timeBurning[row-15][col-15] = 1


# # show grid
# plt.imshow(grid, cmap="jet")
# plt.colorbar()
# plt.show()


# states
# 0 = water
# 1 = sparse, agri
# 2 = sparse, thickets
# 3 = sparse, pines
# 4 = normal, agri
# 5 = normal, thickets
# 6 = normal, pines
# 7 = dense, agri
# 8 = dense, thickets
# 9 = dense, pines
# 10 = fire/burning
# 11 = dead


# constants
Ph = 0.58 #s/m
c1 = 0.045 #s/m
c2 = 0.131 #s/m
V = 8 #m/s

for t in range(time):
    for row in range(1,rows-1):
        for col in range(1,cols-1):

            # keep track of how long a cell has been burning
            if grid[row][col] == 10:
                timeBurning[row][col] += 1

            # allocate Pden and Pveg values depending on the state of a cell (see state list above)
            # sparse
            if grid[row][col] == 1:
                Pden = -0.4
                Pveg = -0.3
            elif grid[row][col] == 2:
                Pden = -0.4
                Pveg = 0
            elif grid[row][col] == 3:
                Pden = -0.4
                Pveg = 0.4
            
            
            # normal
            elif grid[row][col] == 4:
                Pden = 0
                Pveg = -0.3
            elif grid[row][col] == 5:
                Pden = 0
                Pveg = 0
            elif grid[row][col] == 6:
                Pden = 0
                Pveg = 0.4

            # dense
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
            if grid[row+1][col-1] == 10:
                theta = 135
                ft = math.e**(V*c2*(math.cos(theta)-1))
                Pw = ft*math.e**(c1*V)
                Pburn_1 = Ph*(1+Pden)*(1+Pveg)*Pw 

            if grid[row+1][col+1] ==  10:
                theta = 135
                ft = math.e**(V*c2*(math.cos(theta)-1))
                Pw = ft*math.e**(c1*V)
                Pburn_2 = Ph*(1+Pden)*(1+Pveg)*Pw 
                
            if grid[row+1][col] == 10:
                theta = 180
                ft = math.e**(V*c2*(math.cos(theta)-1))
                Pw = ft*math.e**(c1*V)
                Pburn_3 = Ph*(1+Pden)*(1+Pveg)*Pw 

            if grid[row][col-1] == 10:
                theta = 180
                ft = math.e**(V*c2*(math.cos(theta)-1))
                Pw = ft*math.e**(c1*V)
                Pburn_4 = Ph*(1+Pden)*(1+Pveg)*Pw 
                
            if grid[row][col+1] == 10:
                theta = 90
                ft = math.e**(V*c2*(math.cos(theta)-1))
                Pw = ft*math.e**(c1*V)
                Pburn_5 = Ph*(1+Pden)*(1+Pveg)*Pw
            
            if grid[row-1][col-1] == 10:
                theta = 45
                ft = math.e**(V*c2*(math.cos(theta)-1))
                Pw = ft*math.e**(c1*V)
                Pburn_6 = Ph*(1+Pden)*(1+Pveg)*Pw

            if grid[row-1][col+1] == 10:
                theta = 45
                ft = math.e**(V*c2*(math.cos(theta)-1))
                Pw = ft*math.e**(c1*V)
                Pburn_7 = Ph*(1+Pden)*(1+Pveg)*Pw

            if grid[row-1][col] == 10:
                theta = 0
                ft = math.e**(V*c2*(math.cos(theta)-1))
                Pw = ft*math.e**(c1*V)
                Pburn_8 = Ph*(1+Pden)*(1+Pveg)*Pw


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
            if (grid[row][col] != 0 and  grid[row][col] != 10 and grid[row][col] != 11) and \
                (np.random.uniform() < Pburn_1 or np.random.uniform() < Pburn_2 or np.random.uniform() < Pburn_3 or\
                np.random.uniform() < Pburn_4 or np.random.uniform() < Pburn_5 or np.random.uniform() < Pburn_6 or \
                np.random.uniform() < Pburn_7 or np.random.uniform() < Pburn_8):
                
                    grid[row][col] = 10   
                    timeBurning[row][col] += 1                                        

            # after 4 timestep, turn burning cell to dead cell
            # Want na 1 timestep zorgde ervoor dat het vuur echt snel doofde
            # Hier moet dus nog naar worden gekeken
            if timeBurning[row][col] == 5:
                grid[row][col] = 11

plt.figure()
plt.imshow(grid, cmap="jet")
plt.colorbar()
plt.show()