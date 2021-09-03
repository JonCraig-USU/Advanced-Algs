<<<<<<< HEAD
print("Hello World")
=======
import time
import matplotlib.pyplot as plt
import numpy as np

def time():
    return time.time()

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
    if Win(stones-1):
        return 1
    if Win(stones-2):
        return 2

for i in range(1, 200):
    start = time()
    stones = i
    while stones > 0:
        n = Move(stones)
        stones -= n
        # print(stones)
    print('{}: {}'.format(i, time() - start))


<<<<<<< HEAD
# if player1:
#     print("Player 1 wins!")
# else:
#     print("Player 2 wins!")
>>>>>>> 2c3c3cde155cbd133b7c70090842dbd4d3db7c6a
=======
>>>>>>> ea4e4d0d7c74f6b3c862fc582f35d12fd90604ee
