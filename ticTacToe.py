def printBoard(board):
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' ' }
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(theBoard)
def checkWinner(board, player):
    print('Checking if ' + player + ' is a winner...')
    if board['top-L'] == ('X') and board['top-M'] == ('X') and board['top-R'] ==('X'):
        return True
    if board['top-L'] == ('O') and board['top-M'] == ('O') and board['top-R'] ==('O'):
        return True
    if board['mid-L'] == ('X') and board['mid-M'] == ('X') and board['mid-R'] ==('X'):
        return True
    if board['mid-L'] == ('O') and board['mid-M'] == ('O') and board['mid-R'] ==('O'):
        return True
    if board['low-L'] == ('X') and board['low-M'] == ('X') and board['low-R'] ==('X'):
        return True
    if board['low-L'] == ('O') and board['low-M'] == ('O') and board['low-R'] ==('O'):
        return True
    if board['low-L'] == ('X') and board['mid-M'] == ('X') and board['top-R'] ==('X'):
        return True
    if board['low-L'] == ('O') and board['mid-M'] == ('O') and board['top-R'] ==('O'):
        return True
    if board['top-L'] == ('O') and board['mid-M'] == ('O') and board['low-R'] ==('O'):
        return True
    if board['top-L'] == ('X') and board['mid-M'] == ('X') and board['low-R'] ==('X'):
        return True
    if board['low-L'] == ('X') and board['mid-L'] == ('X') and board['top-L'] ==('X'):
        return True
    if board['low-M'] == ('X') and board['mid-M'] == ('X') and board['top-M'] ==('X'):
        return True
    if board['low-R'] == ('X') and board['mid-R'] == ('X') and board['top-R'] ==('X'):
        return True
    if board['low-L'] == ('O') and board['mid-L'] == ('O') and board['top-L'] ==('O'):
        return True
    if board['low-M'] == ('O') and board['mid-M'] == ('O') and board['top-M'] ==('O'):
        return True
    if board['low-R'] == ('O') and board['mid-R'] == ('O') and board['top-R'] ==('O'):
        return True
    else
        return False
    #Hope ^^^ is correct. Was super confused as to how to checkWinner
def startGame(startingPlayer, board):
    # TO DO #################################################################
    # Add comments to each line in this function to describe what           #
    # is happening. You do not need to modify any of the Python code        #
    #########################################################################

    turn = startingPlayer
    #Creates variable turn equal to startingPlayer
    for i in range(9):
        printBoard(board)
    #Prints board at start of new turn
        print('Turn for ' + turn + '. Move on which space?')
        move = input()
    #Asks for player's move
        board[move] = turn
    #Equates move to turn
        if( checkWinner(board, 'X') ):
            print('X wins!')
            break
    #Checks to see if X has won
        elif ( checkWinner(board, 'O') ):
            print('O wins!')
            break
    #Checks to see if O has won
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    #Changes the current player

    printBoard(board)
    #Prints board with updated moves
