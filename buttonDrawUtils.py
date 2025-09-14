import pygame
import sys
from variables import WIDTH, HEIGHT, BG_COLOR, LINE_COLOR, FONT

def draw_button(screen, rect, text, active):
    color = (100, 200, 100) if active else (200, 200, 200)
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, LINE_COLOR, rect, 3)
    label = FONT.render(text, True, LINE_COLOR)
    label_rect = label.get_rect(center=rect.center)
    screen.blit(label, label_rect)


def choose_mode_pygame():
    """
    Окно выбора режима игры через pygame.
    Возвращает: mode (str), bot_symbol (str), bot_difficulty (str)
    """
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # Кнопки
    btn_pvp = pygame.Rect(WIDTH//3 - 100, 150, 400, 50)
    btn_bot = pygame.Rect(WIDTH//3 - 100, 220, 400, 50)

    # Для выбора символа бота (если будет)
    btn_bot_x = pygame.Rect(WIDTH//2 - 100, 300, 90, 50)
    btn_bot_o = pygame.Rect(WIDTH//2 + 10, 300, 90, 50)

    # Для выбора сложности
    btn_easy = pygame.Rect(WIDTH//2 - 100, 400, 90, 50)
    btn_hard = pygame.Rect(WIDTH//2 + 10, 400, 90, 50)

    mode = None
    bot_symbol = 'O'
    bot_difficulty = 'hard'
    selecting_bot_options = False

    running = True
    while running:
        screen.fill(BG_COLOR)

        title = FONT.render("Выберите режим игры", True, LINE_COLOR)
        title_rect = title.get_rect(center=(WIDTH//2, 80))
        screen.blit(title, title_rect)

        pygame.draw.rect(screen, (255, 0, 0), btn_pvp, 2)  # красный контур pvp
        pygame.draw.rect(screen, (0, 0, 255), btn_bot, 2)  # синий контур bot

        # Отрисовка кнопок выбора режима
        draw_button(screen, btn_pvp, "Игрок против Игрока", mode == 'pvp')
        draw_button(screen, btn_bot, "Игрок против Бота", mode == 'bot' or selecting_bot_options)

        if mode == 'bot' or selecting_bot_options:
            # Выбор символа
            label = FONT.render("За кого играет бот?", True, LINE_COLOR)
            screen.blit(label, (WIDTH//2 - 100, 270))
            draw_button(screen, btn_bot_x, "X", bot_symbol == 'X')
            draw_button(screen, btn_bot_o, "O", bot_symbol == 'O')

            # Выбор сложности
            label2 = FONT.render("Сложность", True, LINE_COLOR)
            screen.blit(label2, (WIDTH//2 - 100, 370))
            draw_button(screen, btn_easy, "easy", bot_difficulty == 'easy')
            draw_button(screen, btn_hard, "hard", bot_difficulty == 'hard')

            # Инструкция
            instr = FONT.render("Нажмите Enter, чтобы начать", True, LINE_COLOR)
            instr_rect = instr.get_rect(center=(WIDTH//2, HEIGHT - 50))
            screen.blit(instr, instr_rect)
        else:
            instr = FONT.render("Кликните для выбора режима", True, LINE_COLOR)
            instr_rect = instr.get_rect(center=(WIDTH//2, HEIGHT - 50))
            screen.blit(instr, instr_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = event.pos
                if btn_pvp.collidepoint(pos):
                    mode = 'pvp'
                    selecting_bot_options = False
                elif btn_bot.collidepoint(pos):
                    mode = 'bot'
                    selecting_bot_options = True  # Показываем опции бота


                elif selecting_bot_options:
                    if btn_bot_x.collidepoint(pos):
                        bot_symbol = 'X'
                    elif btn_bot_o.collidepoint(pos):
                        bot_symbol = 'O'
                    elif btn_easy.collidepoint(pos):
                        bot_difficulty = 'easy'
                    elif btn_hard.collidepoint(pos):
                        bot_difficulty = 'hard'

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and mode is not None:
                    # Подтверждение выбора — запускаем игру
                    running = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        clock.tick(30)

    return mode, bot_symbol, bot_difficulty