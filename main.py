"""
Tic-Tac-Toe (крестики-нолики) на pygame
- Локальный мультиплеер или игра против бота (easy/hard)
- Нажмите R чтобы перезапустить, ESC чтобы выйти

Запуск:
pip install pygame
python tic_tac_toe_pygame.py
"""
import sys
from pygameUtils import *
from botFunctions import *
from buttonDrawUtils import *


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Крестики-нолики — мультиплеер/бот")


def reset_game():
    global board, current_player, game_over, winner
    board = [['' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    game_over = False
    winner = None

def choose_mode():
    global mode, bot_symbol, bot_difficulty
    mode, bot_symbol, bot_difficulty = choose_mode_pygame()

def main_loop():
    global game_over, winner, current_player
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:
                    reset_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and mode == 'pvp':
                    handle_click(event.pos)
                elif event.button == 1 and mode == 'bot' and current_player != bot_symbol:
                    handle_click(event.pos)

        if mode == 'bot' and current_player == bot_symbol and not game_over:
            bot_move()

        draw_board()
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    choose_mode()
    main_loop()
