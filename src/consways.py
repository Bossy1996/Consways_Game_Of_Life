# Conway's game of life

import random, time, copy

WIDTH = 60
HEIGHT = 20

#Create a list of list for the cells.

nextCells = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#') #creates a living cell
        else:
            column.append(' ') #adds a dead cell
    nextCells.append(column) #next cells is a list of column lists.

while True: # Main program loop
    print('\n\n\n\n\n') # Separate each step with new lines.
    currentCells = copy.deepcopy(nextCells)
    #print currentCells on the screen.
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') #prints the # or space
        print() #print a newline at the end of the row.

    #Calculate the next step's cells based on current step's cells.
    for x in range(WIDTH):
        for y in range(HEIGHT):
            #get neighboring coordinates
            # `% WIDTH` ensures lefCoord is always between 0 and WIDTH -1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoor = (y + 1) % HEIGHT

            #Count numebr of living neighbors
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] = '#':
                numNeighbors += 1 # Top-Left neighbor is alive.
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 #Top neighbor is alive.
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-Right neighbor is alive.
            if currentCells[leftCoord][y] == '#':
                currentCells +=1 # Left neighbor is alive.
            if currentCells[rightCoord][y] == '#':
                currentCells += 1 # Right neighbor is alive.
            if currentCells[leftCoord][belowCoor] == '#':
                currentCells += 1 # Below-left neighbor is alive.
            if currentCells[x][belowCoor] == '#':
                currentCells += 1 # Below neighbor is alive.
            if currentCells[rightCoord][belowCoor] == '#':
                currentCells += 1 # Reight-below neighbor is alive.
            
            #Set cell based on Conway's Game of live rules
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                #living cells with 2 or 3 neighbors stay alive
                nextCells[x][y] = '#'
            elif currentCells[x][y] == '' and numNeighbors == 3:
                #Dead cells with 3 neighbors become alive
                nextCells[x][y] = '#'
            else:
                nextCells[x][y] = ''
        time.sleep(1) # Add a 1-second pause to reduce flickering.