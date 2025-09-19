"""
Tic-Tac-Toe (крестики-нолики) на pygame
- Локальный мультиплеер или игра против бота (easy/hard)
- Нажмите R чтобы перезапустить, ESC чтобы выйти

Запуск:
pip install pygame
python tic_tac_toe_pygame.py
"""



import pygame as pygame
from pygameUtils import *
import botFunctions
from buttonDrawUtils import *
from variables import *


pygame.init()
pygame.display.set_caption("Крестики-нолики — мультиплеер/бот")

def choose_mode():
    choose_mode_pygame()

def main_loop():

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:
                    running = False
                    variables.restart = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and mode == 'pvp':
                    handle_click(event.pos)
                elif event.button == 1 and mode == 'bot' and variables.current_player != variables.bot_symbol:
                    handle_click(event.pos)

        if variables.mode == 'bot' and variables.current_player == variables.bot_symbol and not variables.game_over:
            botFunctions.bot_move()

        draw_board()
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

def run():
    choose_mode()
    main_loop()
    if restart:
        choose_mode()
        main_loop()


if __name__ == '__main__':
    run()
