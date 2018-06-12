import pygame

from score import calculate_points


def init_board(display, cols, rows):
    background = pygame.Surface(display.get_size())
    background.convert()
    background.fill((255, 255, 255))

    width = cols * 30
    height = rows * 30

    # draw rectangle with board
    pygame.draw.line(background, (0, 0, 0), (0, 0), (width, 0), 1)
    pygame.draw.line(background, (0, 0, 0), (width, 0), (width, height), 1)
    pygame.draw.line(background, (0, 0, 0), (width, height), (0, height), 1)
    pygame.draw.line(background, (0, 0, 0), (0, height), (0, 0), 1)


    # draw horizontal lines
    for i in range(0, height, 30):
        pygame.draw.line(background, (0, 0, 0), (0, i), (width, i), 1)

    # draw vertical lines
    for i in range(0, width, 30):
        pygame.draw.line(background, (0, 0, 0), (i, 0), (i, height), 1)

    return background


def show_board(display, board, score):
    draw_status(display, board, score)
    display.blit(board, (0, 0))
    pygame.display.flip()


def board_position(mouse_x, mouse_y):
    col = int(mouse_x / 30)
    row = int(mouse_y / 30)
    return (col, row)


def draw_move(board, col, row, player, grid):
    center_x = col * 30 + 15
    center_y = row * 30 + 15

    if player == 1:
        color = (255, 0, 0)
    else:
        color = (0, 0, 255)

    pygame.draw.circle(board, color, (center_x, center_y), 10, 0)
    grid[row][col] = player


def draw_status(display, board, score):
    x, y = display.get_size()
    message = 'P1: {} | P2: {}'.format(score[1], score[2])
    # render the status message
    font = pygame.font.Font(None, 24)
    text = font.render(message, 1, (10, 10, 10))

    # copy the rendered message onto the board
    board.fill((255, 0, 0), (x - 185, 5, 180, 40))
    board.blit(text, (x - 180, 10))


def click_board(board, grid, human_turn, scoreboard):
    # human will always be first, so player 1 is human
    player = 1
    (mouse_x, mouse_y) = pygame.mouse.get_pos()
    (col, row) = board_position(mouse_x, mouse_y)
    try:
        if grid[row][col] != 0 or not human_turn:
            return False, None, None
    except IndexError:
        return False, None, None
    scoreboard[player] += calculate_points(player, grid, col, row, permanent=True)
    draw_move(board, col, row, player, grid)
    return True, col, row


def ai_move(board, grid, scoreboard, col, row):
    # human will always be first, so player 1 is human
    player = 2
    print(row, col, grid[row][col])
    if grid[row][col] != 0:
        return False, None, None
    scoreboard[player] += calculate_points(player, grid, col, row, permanent=True)
    draw_move(board, col, row, player, grid)
    return True, col, row
