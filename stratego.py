#!/usr/bin/python
import argparse
import pygame
import time
from pygame.constants import QUIT, MOUSEBUTTONDOWN

from ai import minmax, Node
from board import init_board, show_board, click_board, draw_move, ai_move

grid = None


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run game')
    parser.add_argument('--size', dest='size')
    args = parser.parse_args()
    board_size = int(args.size)

    pygame.init()
    display = pygame.display.set_mode((board_size*30 + 200,
                                       board_size*30))
    pygame.display.set_caption('Stratego')

    board = init_board(display, board_size, board_size)

    grid = [[0 for _ in range(board_size)] for _ in range(board_size)]
    scoreboard = {1: 0, 2: 0}

    human_turn = True
    node = None
    depth = 0
    player = 1

    while True:
        for event in pygame.event.get():
            if event.type is QUIT:
                break
            elif event.type is MOUSEBUTTONDOWN:
                successful_move, col, row = click_board(board, grid, human_turn, scoreboard)
                depth += 1
                if successful_move:
                    human_turn = not successful_move
                    node = Node(grid, col, row)
                    node, _ = minmax(2, node, depth+1)
                    human_turn, col, row = ai_move(board, grid, scoreboard, node.col, node.row)
                for i in grid:
                    print(i)

        show_board(display, board, scoreboard)
