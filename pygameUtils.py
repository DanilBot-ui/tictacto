from pygame import Rect

from main import *



def draw_board():
    # фон
    screen.fill(BG_COLOR)

    # подсказка сверху
    title = BIG_FONT.render("Крестики-нолики — PvP или Бот", True, LINE_COLOR)
    title_rect = title.get_rect(center=(WIDTH//2, 20))
    screen.blit(title, title_rect)

    # сетка
    for i in range(1, 3):
        # вертикальные линии
        start_pos = (BOARD_LEFT + i * CELL_SIZE, BOARD_TOP)
        end_pos = (BOARD_LEFT + i * CELL_SIZE, BOARD_TOP + BOARD_SIZE)
        pygame.draw.line(screen, LINE_COLOR, start_pos, end_pos, LINE_WIDTH)
        # горизонтальные линии
        start_pos = (BOARD_LEFT, BOARD_TOP + i * CELL_SIZE)
        end_pos = (BOARD_LEFT + BOARD_SIZE, BOARD_TOP + i * CELL_SIZE)
        pygame.draw.line(screen, LINE_COLOR, start_pos, end_pos, LINE_WIDTH)

    # фигурки
    for r in range(3):
        for c in range(3):
            val = board[r][c]
            cell_rect = Rect(BOARD_LEFT + c * CELL_SIZE, BOARD_TOP + r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if val == 'X':
                draw_x(cell_rect)
            elif val == 'O':
                draw_o(cell_rect)

    # текущий игрок / сообщение
    if game_over:
        if winner == 'Draw':
            msg = "Ничья!"
        else:
            msg = f"Победил {winner}!"
        sub = FONT.render(msg, True, LINE_COLOR)
        sub_rect = sub.get_rect(center=(WIDTH//2, BOARD_TOP + BOARD_SIZE + 40))
        screen.blit(sub, sub_rect)

        instr = FONT.render("Нажмите R чтобы начать заново, Esc чтобы выйти", True, LINE_COLOR)
        instr_rect = instr.get_rect(center=(WIDTH//2, BOARD_TOP + BOARD_SIZE + 80))
        screen.blit(instr, instr_rect)
    else:
        msg = f"Ход: {current_player}"
        sub = FONT.render(msg, True, LINE_COLOR)
        sub_rect = sub.get_rect(center=(WIDTH//2, BOARD_TOP + BOARD_SIZE + 40))
        screen.blit(sub, sub_rect)

        instr = FONT.render("R — перезапустить, Esc — выйти", True, LINE_COLOR)
        instr_rect = instr.get_rect(center=(WIDTH//2, BOARD_TOP + BOARD_SIZE + 80))
        screen.blit(instr, instr_rect)


def draw_x(rect: Rect):
    padding = CELL_PADDING
    x1, y1 = rect.topleft
    x2, y2 = rect.bottomright
    pygame.draw.line(screen, X_COLOR, (x1 + padding, y1 + padding), (x2 - padding, y2 - padding), 12)
    pygame.draw.line(screen, X_COLOR, (x1 + padding, y2 - padding), (x2 - padding, y1 + padding), 12)


def draw_o(rect: Rect):
    cx = rect.left + rect.width // 2
    cy = rect.top + rect.height // 2
    radius = rect.width // 2 - CELL_PADDING
    pygame.draw.circle(screen, O_COLOR, (cx, cy), radius, 12)


def handle_click(pos):
    global current_player, game_over, winner
    if game_over:
        return
    x, y = pos
    if x < BOARD_LEFT or x > BOARD_LEFT + BOARD_SIZE or y < BOARD_TOP or y > BOARD_TOP + BOARD_SIZE:
        return
    c = (x - BOARD_LEFT) // CELL_SIZE
    r = (y - BOARD_TOP) // CELL_SIZE
    r = int(r)
    c = int(c)
    if board[r][c] == '':
        board[r][c] = current_player
        winner = check_winner()
        if winner is not None:
            game_over = True
        else:
            current_player = 'O' if current_player == 'X' else 'X'

