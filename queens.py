GRID_SIZE = 8


def is_valid(columns, row, column):
    for row2 in range(row):
        col2 = columns[row2]

        if col2 == column:
            return False

        if abs(col2 - column) == abs(row2 - row):
            return False

    return True


def place(row, columns, results):
    if row == GRID_SIZE:
        results.append(list(columns))
    else:
        for column in range(GRID_SIZE):
            if is_valid(columns, row, column):
                columns[row] = column
                place(row + 1, columns, results)


cols = [0] * 8
row = 0
res = []

place(row, cols, res)

print(res)
