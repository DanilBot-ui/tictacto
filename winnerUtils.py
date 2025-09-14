from main import *
from variables import *

def check_winner():
    # возвращает 'X', 'O', 'Draw' или None
    for combo in WIN_COMBINATIONS:
        vals = [board[r][c] for r,c in combo]
        if vals[0] != '' and vals.count(vals[0]) == 3:
            return vals[0]
    # check draw
    for r in range(3):
        for c in range(3):
            if board[r][c] == '':
                return None
    return 'Draw'



def check_winner_state(state):
    for combo in WIN_COMBINATIONS:
        vals = [state[r][c] for r,c in combo]
        if vals[0] != '' and vals.count(vals[0]) == 3:
            return vals[0]
    for r in range(3):
        for c in range(3):
            if state[r][c] == '':
                return None
    return 'Draw'