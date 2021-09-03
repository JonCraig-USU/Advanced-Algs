def Nim():
    stones = input("How many stones would you like to play with? ")
    while stones >= 0:
        if stones == 0:
            return print("Player 1 wins!")
        p1 = input("Player 1: Pick a number 1 or 2: ")
        stones -= int(p1)
        print(stones)
        
        if stones == 0:
            return print("Player 2 wins!")
        p2 = Move(stones)
        print("Player 2 chose: " + p2 + " to take")
        stones -= p2
        print(stones)    

def Move(stones):
    '''
    @Return number of stones to take
    '''
    if stones == 1:
        return 1
    if stones == 2:
        return 1
    if win(stones-1):
        return 1
    if win(stones-2):
        return 2

def Win(stones):
    '''
    @Returns boolean for win condition based on if opponent will lose
    '''
    if stones == 0:
        return True
    if stones == 1:
        return False
    return not(Win(stones-1) and Win(n-2))