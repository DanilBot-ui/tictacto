from main import *
from winnerUtils import *
import random

def random_bot_move():
    choices = [(r, c) for r in range(3) for c in range(3) if board[r][c] == '']
    return random.choice(choices)


def minimax(board_state, player, maximizing, bot_symbol):
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
                    score, _ = minimax(board_state, player, False, bot_symbol)
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
                    score, _ = minimax(board_state, player, True, bot_symbol)
                    board_state[r][c] = ''
                    if score < best_score:
                        best_score = score
                        best_move = (r, c)
        return best_score, best_move

def hard_bot_move():
    _, move = minimax([row[:] for row in board], bot_symbol, True, bot_symbol)
    if move is None:
        return random_bot_move()
    return move


def bot_move():
    global current_player, game_over, winner
    if game_over:
        return
    if current_player == bot_symbol:
        if bot_difficulty == 'easy':
            r, c = random_bot_move()
        else:
            r, c = hard_bot_move()
        board[r][c] = bot_symbol
        winner = check_winner()
        if winner is not None:
            game_over = True
        else:
            current_player = 'O' if current_player == 'X' else 'X'

