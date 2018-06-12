

def calculate_points(player, grid, col, row, depth=0, permanent=False):
    grid[row][col] = player
    size = len(grid)
    points = 0
    _points = 0

    # check row
    for i in range(size):
        if grid[row][i] != 0:
            _points += 1
        else:
            _points = 0
            break
    points += _points

    # check col
    for i in range(size):
        if grid[i][col] != 0:
            _points += 1
        else:
            _points = 0
            break
    points += _points

    # check diagonal ltr utd
    l = []
    c = col
    r = row
    while c <= size - 1 and r <= size - 1:
        l.append(grid[r][c])
        c += 1
        r += 1

    c = col - 1
    r = row - 1
    while c >= 0 and r >= 0:
        l.append(grid[r][c])
        c -= 1
        r -= 1
    if len(l) > 1 and all([i != 0 for i in l]):
        points += len(l)

    l = []

    c = col
    r = row
    while c >= 0 and r <= size - 1:
        l.append(grid[r][c])
        c -= 1
        r += 1

    c = col + 1
    r = row - 1
    while c <= size - 1 and r >= 0:
        l.append(grid[r][c])
        c += 1
        r -= 1

    if len(l) > 1 and all([i != 0 for i in l]):
        points += len(l)

    if not permanent:
        grid[row][col] = 0
    return points or -depth
