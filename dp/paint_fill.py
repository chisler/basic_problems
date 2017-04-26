r = [[0, 0, 1],
     [0, 0, 0]]


def paint(x, y, origin, new_color):
    if not 0<=x<len(r[0]) or not 0<=y<len(r) or r[y][x] != origin:
        return

    r[y][x] = new_color

    for i in range(-1, 2):
        for j in range(-1, 2):
            paint(x + i, y + j, origin, new_color)


paint(2, 0, 1, 3)
print(r)