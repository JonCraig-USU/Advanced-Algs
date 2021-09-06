import time
import matplotlib.pyplot as plt
import numpy as np

# Recursive Functions
def Win(stones):
    '''
    @Returns boolean for win condition based on if opponent will lose
    '''
    if stones == 0:
        return True
    if stones == 1:
        return False
    return not(Win(stones-1) and Win(stones-2))

def Move(stones):
    '''
    @Return number of stones to take
    '''
    if stones == 1:
        return 1
    if stones == 2:
        return 1
    if not Win(stones-1):
        return 1
    if not Win(stones-2):
        return 2
    return 2

# Memoizing version of win condition
def WinMem(stones):
    # alocate memory
    sol = [False] * (stones + 1)
    #fill simple prob/solution
    sol[0] = True
    # fill all solutions
    for j in range(2, stones + 1):
        sol[j] = not(sol[j-1] and sol[j - 2])
    return sol[stones]

# set variables and arrays for the recursive solution
xValues = []
x = 0
times = []
begin = time.time()

# While loop for time controlled ending
while (time.time() - begin) < 1200:
    stones = x
    start = time.time()
    while stones > 0:
        n = Move(stones)
        stones -= n
    print('{}: {}'.format(x, time.time() - start))
    times.append(time.time() - start)
    xValues.append(x)
    x += 1
print("Time: " + str(time.time() - begin))

# variables and calculation for best fit line
bestX = np.asanyarray(xValues)
bestY = np.asanyarray(times)
m, b = np.polyfit(bestX, bestY, 1)

# calculate the best fit line y values
lineY = []
for entry in bestX:
    lineY.append(m * entry + b)

# set the graph info
plt.plot(xValues, times, 'ro', xValues, lineY, '-')
plt.yscale('log')

# label the graph and axes
plt.title("Nim")
plt.xlabel("Number of Stones")
plt.ylabel("Time")

# draw the graph
plt.show()
print("Slope: " + str(m))

# Check that the solutions match
for k in range(0, 35):
    norm = Win(k)
    mem = WinMem(k)
    if mem != norm:
        print('Got another error Captain')
        print('{}: {}'.format(norm, mem))





