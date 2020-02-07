# JOGO DA VELHA

def displayBoard(board):
    print('    |   |    \n  {} | {} |  {}  \n    |   |    '.format(board[7],board[8],board[9]))
    print('-------------')
    print('    |   |    \n  {} | {} |  {}  \n    |   |    '.format(board[4],board[5],board[6]))
    print('-------------')
    print('    |   |    \n  {} | {} |  {}  \n    |   |    '.format(board[1],board[2],board[3]))

displayBoard(['#','X','0','X','0','X','0','X','0','X'])


def playerInput():
    marker = ''
    while (marker != 'X' and marker != 'O'):
        marker = input('Player 1, marcar com X ou O?\n').upper()

    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1,player2)

player1, player2 = playerInput()

def placeMarker(board,marker,position):
    board[position] = marker

testBoard = ['#','X','0','X','0','X','0','X','0','X']
placeMarker(testBoard,'$',8)
displayBoard(testBoard)

def winCheck(board):
    return ( (board[1]==board[2]==board[3]) or (board[4]==board[5]==board[6]) or (board[7]==board[8]==board[9]) or (board[1]==board[4]==board[7]) or (board[2]==board[5]==board[8]) or (board[3]==board[6]==board[9]) or (board[1]==board[5]==board[9]) or (board[3]==board[5]==board[7]) ) 

winCheck(testBoard)

import random

def chooseFirst():
    flip = random.randint(0,1)
    return 'Player 1' if flip==0 else 'Player 2'

# chooseFirst()

def spaceCheck(board,position):
    return board[position] == ' '

def fullBoardChech(board):
    for i in range(1,10):
        if spaceCheck(board,i):
            return False
    
    return True

def playerChoice(board):
    position = 0
    while position not in range(1,10) or not spaceCheck(board,position):
        position = int(input('Escolha uma posicao entre 1 e 9: '))

    return position

def replay():
    choice = input('Jogar novamente? Y/N\n').upper
    return choice == 'Y'




i = 0
while i < 30:
    print('\n')
    i += 1

print('Bem-vindo ao Jogo da Velha!')

while True:
    
    theBoard = [ ' ' ]*10
    player_1,player_2 = playerInput()
    
    turn = chooseFirst() 
    print(turn+' joga primeiro\n')
    
    if input('Preparados? Y/N').upper == 'Y':
        game_on = True
    else:
        game_on = False
    
    while game_on:

        if turn == 'Player 1':
            displayBoard(theBoard)
            position = playerChoice(theBoard)
            placeMarker(theBoard,player_1,position)

            if winCheck(theBoard):
                displayBoard(theBoard)
                print('\n\n'+turn+' venceu!\n')
                game_on = False
            else:
                if fullBoardChech(theBoard):
                    displayBoard(theBoard)
                    print('\n\nO jogo empatou!\n')
                    game_on = False
                else:
                    turn = 'Player 2'

        else:
            displayBoard(theBoard)
            position = playerChoice(theBoard)
            placeMarker(theBoard,player_2,position)

            if winCheck(theBoard):
                displayBoard(theBoard)
                print('\n\n'+turn+' venceu!\n')
                game_on = False
            else:
                if fullBoardChech(theBoard):
                    displayBoard(theBoard)
                    print('\n\nO jogo empatou!\n')
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break
