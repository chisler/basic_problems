


def robot(grid, x, y, path):
    if x > len(grid[0]) - 1 or y > len(grid) - 1:
        return

    if grid[y][x] == 1:
        return

    grid[y][x] = 1

    if x == len(grid[-1]) - 1 and y == len(grid) - 1:
        print(path + "({}, {})".format(x, y))
        return

    robot(grid, x + 1, y, path + "({}, {})".format(x, y))
    robot(grid, x, y + 1, path + "({}, {})".format(x, y))


r = [[0, 0, 1],
    [0, 0, 0]]

robot(r, 0, 0, '')