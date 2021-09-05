import time
import matplotlib.pyplot as plt
import numpy as np


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



xValues = []
x = 0
times = []
begin = time.time()

while (time.time() - begin) < 600:
    stones = x
    start = time.time()
    while stones > 0:
        n = Move(stones)
        stones -= n
    print('{}: {}'.format(x, time.time() - start))
    times.append(time.time() - start)
    xValues.append(x)
    x += 1

bestX = np.asanyarray(xValues)
bestY = np.asanyarray(times)
m, b = np.polyfit(bestX, bestY, 1)

# set the graph info
plt.plot(xValues, times, 'ro', xValues, m*xValues+b, '-')
plt.yscale('log')

# label the graph and axes
plt.title("Nim")
plt.xlabel("Number of Stones")
plt.ylabel("Time")

# draw the graph
plt.show()




