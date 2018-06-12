import copy
import random

from score import calculate_points


class Node(object):

    def __init__(self, grid, col, row, player=1):
        grid[row][col] = player
        self.col = col
        self.row = row
        self.grid = grid
        self.size = len(self.grid)

    def children(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.grid[row][col] == 0:
                    _grid = copy.deepcopy(self.grid)
                    _grid[row][col] = -1
                    yield Node(_grid, col, row)


def minmax(player, node, depth):
    return alphabeta(player, node, depth, -float('inf'), float('inf'))


def alphabeta(player, node, depth, alpha, beta):
    if depth % 3 ==0 or not list(node.children()):
        return node, calculate_points(player, node.grid, node.col, node.row, depth)

    if player == 1:
        for child in node.children():
            node, ab = alphabeta(2, child, depth+1, alpha, beta)
            beta = min(beta, ab)
            if alpha >= beta:
                break
        return node, beta
    else:
        for child in node.children():
            node, ab = alphabeta(1, child, depth+1, alpha, beta)
            alpha = max(alpha, ab)
            if alpha >= beta:
                break
        return node, alpha
