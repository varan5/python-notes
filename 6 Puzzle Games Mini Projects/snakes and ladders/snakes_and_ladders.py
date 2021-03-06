#snakes and ladders
import random

def create_board(players):
    board = [] # a list (dynamic array)
    for i in range(100): #0-99
        element = [i+1, [' ']*players , ' '] # [number, pegs[], sym]
        board.append(element)
    return board

def display_board(board):
    print()
    i, x, flag = 1, 99, 0

    while i <=10:
        print() #row change : rendered by bringing cursor on the next line
        j = 1
        while j <= 10:
            # element printing
            print(board[x], end= ' ')
            x = x -1 if flag == 0 else x+1  #var = valOnTrue if condn else valOnFalse
            j+=1

        x = x -9 if flag == 0 else x - 11
        flag = (flag+1)%2
        i+=1
    print()


def dice(isBot=False):
    totVal = 0
    for i in range(3): #max 3 chances
        #rendering
        if not isBot:
            if i == 0:
                _ = input('Press enter to dice')
            else:
                _ = input('Redice as you got 6')
        else:
            if i == 0:
                print('Bot dices ')
            else:
                print('Bot redices as it got 6 ')

        #dicing logic
        currVal = random.randint(1,6) # a random value in range 1-6
        totVal += currVal
        if currVal != 6:
            break
    return totVal % 18


#167: Snake Head
#187 : Snake Body
#191: Snake Tail
def draw_snakes(board, snakes):
    for asnake in snakes:
        sz = len(asnake)
        for i in range(sz):
            if i == 0:
                board[asnake[i]][2] = chr(167)
            elif i == sz-1:
                board[asnake[i]][2] = chr(191)
            else:
                board[asnake[i]][2] = '||'



# 84 : Ladder Top
# 166  : Ladder Body
# 72 : Ladder Bottom

def draw_ladders(board, ladders):
    for aladder in ladders:
        sz = len(aladder)
        for i in range(sz):
            if i == 0:
                board[aladder[i]][2] = chr(72)
            elif i == sz-1:
                board[aladder[i]][2] = chr(84)
            else:
                board[aladder[i]][2] = chr(166)



def snakes_and_ladders(): #GAME
    #snakes definition
    snakes = [ [96,83,76,63,56,43,36,23,16], [60,59,40,39,20] , [65,54,45,34,25,14], [69,50,49,30,29,10,9]]
    snake_bite = {96:16,60:20, 65:14, 69:9 }

    #ladders definition
    ladders = [ [11,28,31,48,51,68], [27,32,47,52,67,72,87], [34,45,54,65], [42,57,62,77,82,97] ]
    ladder_rise = {11:68,27:87, 34:65, 42:97}

    #how many players?
    playerCount = int(input('Enter the number players (1-4) '))

    #validation
    if playerCount < 1 or playerCount > 4:
        print('Invalid Player Count')
        return

    #bot option
    botPlaying = False #flag
    if playerCount < 4:
        ch = input('Do you want to play with the System? (y/n) ')
        if ch == 'y' or ch == 'Y':
            botPlaying = True
            playerCount+=1

    if playerCount == 1:
        print('Insufficient Players')
        return

    #define the board
    board = create_board(playerCount)

    #draw snakes
    draw_snakes(board, snakes)
    #draw ladders
    draw_ladders(board, ladders)


    #define the players
    players_symbols = [] #sym1(♥), sym2 (♦), ...
    players_score = []

    # distribute the pegs
    pegs = ['♥','♦','♣','♠'] #Alt+3, Alt+4, Alt+5, Alt+6

    for i in range(playerCount): #for playerCount number of times
        players_symbols.append(pegs[i])
        players_score.append(-1) #to ensure that default loc is behind value 1, 0 is the index of value 1

    #lets play
    current = 0
    rank = 1
    while playerCount > 1:
        print(players_symbols[current], 'plays ')
        diceValue = dice(current == playerCount-1 and botPlaying)
        print(players_symbols[current], 'got', diceValue)

        temp =  players_score[current] + diceValue

        if temp > 99: #value 100
            print('Chance void')
            print(players_symbols[current], 'needs', 99- players_score[current])
        elif temp in snake_bite.keys():
            print(players_symbols[current] , 'bitten by snake @', temp + 1)
            print(players_symbols[current] , 'falls to', snake_bite[temp]  +1)
            #erase the peg from original position
            board[players_score[current]][1][current] = ' '
            #apply the sanke byte to the score
            players_score[current] = snake_bite[temp]
            #draw the peg at new position
            board[players_score[current]][1][current]= players_symbols[current]

        elif temp in ladder_rise.keys():
            print(players_symbols[current] , 'gets a ladder @', temp + 1)
            print(players_symbols[current] , 'rises to', ladder_rise[temp] + 1 )
            #erase the peg from original position
            board[players_score[current]][1][current] = ' '
            #apply the ladder rise to the score
            players_score[current] = ladder_rise[temp]
            #draw the peg at new position
            board[players_score[current]][1][current]= players_symbols[current]

        else:
            #erase the peg from original position
            board[players_score[current]][1][current] = ' '
            #apply the diceValue to the score
            players_score[current] += diceValue
            #draw the peg at new position
            board[players_score[current]][1][current]= players_symbols[current]

        #render
        display_board(board)

        #winning
        if players_score[current] == 99: #value 100
            if current == playerCount -1: #bot
                botPlaying = False

            print(players_symbols[current], 'WINS !!!')
            print('Rank: ', rank)
            rank+=1
            #remove the player
            players_symbols.pop(current)
            players_score.pop(current)
            #reduce the player count
            playerCount-=1

        #change the player
        current = (current+1) % playerCount

    print(players_symbols[0], 'LOSES!!!')



def main():
    snakes_and_ladders()

main()
