"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    numX = board[0].count(X) + board[1].count(X) + board[2].count(X)
    numO = board[0].count(O) + board[1].count(O) + board[2].count(O)
    
    if numX > numO or numX == 0 :
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    return {(i, j) for i, row in enumerate(board) for j, value in enumerate(row) if value is None}
    
    


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    (i,j)= action
    if board[i][j] != None :
        raise ValueError
    elif player(board) == X:
        deepboard = copy.deepcopy(board)
        board[i][j] = X
    else:
        deepboard = copy.deepcopy(board)
        board[i][j] = O

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] in ['X', 'O']:
            return board[i][0]
        
        # Check columns
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] in ['X', 'O']:
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] in ['X', 'O']:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] in ['X', 'O']:
        return board[0][2]

    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    Return winner(board) != None or actions(board) == set()



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

