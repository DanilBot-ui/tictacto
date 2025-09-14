import random
from winnerUtils import check_winner_state

def random_bot_move(board_state):
    choices = [(r, c) for r in range(3) for c in range(3) if board_state[r][c] == '']
    if choices:
        return random.choice(choices)
    return None, None

def minimax(board_state, bot_symbol, maximizing):
    opp = 'O' if bot_symbol == 'X' else 'X'
    result = check_winner_state(board_state)
    if result == bot_symbol:
        return 1, None
    elif result == opp:
        return -1, None
    elif result == 'Draw':
        return 0, None

    if maximizing:
        best_score = -2
        best_move = None
        for r in range(3):
            for c in range(3):
                if board_state[r][c] == '':
                    board_state[r][c] = bot_symbol
                    score, _ = minimax(board_state, bot_symbol, False)
                    board_state[r][c] = ''
                    if score > best_score:
                        best_score = score
                        best_move = (r, c)
        return best_score, best_move
    else:
        best_score = 2
        best_move = None
        for r in range(3):
            for c in range(3):
                if board_state[r][c] == '':
                    board_state[r][c] = opp
                    score, _ = minimax(board_state, bot_symbol, True)
                    board_state[r][c] = ''
                    if score < best_score:
                        best_score = score
                        best_move = (r, c)
        return best_score, best_move

def hard_bot_move(board_state, bot_symbol):
    _, move = minimax([row[:] for row in board_state], bot_symbol, True)
    if move is None:
        return random_bot_move(board_state)
    return move

def bot_move(board_state, bot_symbol, bot_difficulty):
    if bot_difficulty == 'easy':
        return random_bot_move(board_state)
    else:
        return hard_bot_move(board_state, bot_symbol)