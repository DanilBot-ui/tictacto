import pygame

WIDTH, HEIGHT = 800, 700  # дополнительная полоса для подсказок
LINE_COLOR = (30, 30, 30)
BG_COLOR = (245, 245, 245)
X_COLOR = (66, 133, 244)
O_COLOR = (219, 68, 55)
LINE_WIDTH = 8
CELL_PADDING = 20
FPS = 60

restart = False

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
pygame.init()
FONT = pygame.font.SysFont(None, 36)
BIG_FONT = pygame.font.SysFont(None, 48)

# Игровое поле 3x3
board = [['' for _ in range(3)] for _ in range(3)]
current_player = 'X'  # X ходит первым
game_over = False
winner = None

mode = 'None'  # 'pvp' или 'bot'
bot_symbol = 'O'
bot_difficulty = 'hard'

# Размеры и позиции
BOARD_TOP = 50
BOARD_SIZE = 500
CELL_SIZE = BOARD_SIZE // 3
BOARD_LEFT = (WIDTH - BOARD_SIZE) // 2

WIN_COMBINATIONS = [
    [(0,0),(0,1),(0,2)],
    [(1,0),(1,1),(1,2)],
    [(2,0),(2,1),(2,2)],
    [(0,0),(1,0),(2,0)],
    [(0,1),(1,1),(2,1)],
    [(0,2),(1,2),(2,2)],
    [(0,0),(1,1),(2,2)],
    [(0,2),(1,1),(2,0)],
]






