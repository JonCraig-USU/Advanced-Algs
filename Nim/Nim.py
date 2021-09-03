<<<<<<< HEAD
print("Hello World")
=======
import time

def milliseconds():
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

# stones = input("How many stones would you like to play with? ")
# while stones >= 0:
#     if stones == 0:
#         print("Player 1 wins!")
#         break 
#     p1 = input("Player 1: Pick a number 1 or 2: ")
#     stones -= int(p1)
#     print(stones)
        
#     if stones == 0:
#         print("Player 2 wins!")
#         break
#     p2 = Move(stones)
#     print("Player 2 chose: to take: " + str(p2))
#     stones -= p2
#     print(stones)  

for i in range(1, 200):
    start = milliseconds()
    player1 = True
    stones = i
    while stones > 0:
        n = Move(stones)
        stones -= n
        print(stones)
        player1 != player1
    print('{}: {}'.format(i, milliseconds() - start))


# if player1:
#     print("Player 1 wins!")
# else:
#     print("Player 2 wins!")
>>>>>>> 2c3c3cde155cbd133b7c70090842dbd4d3db7c6a
