def zero(m):
    def clear_row(m, row):
        for col in range(len(m[row])):
            m[row][col] = 0

    def clear_col(m, col):
        for row in range(len(m)):
            m[row][col] = 0

    rows = set()
    cols = set()

    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 0:
                rows.add(i)
                cols.add(j)

    for row in rows:
        clear_row(m, row)
    for col in cols:
        clear_col(m, col)

    return m


def print_m(m):
    for a in m:
        print(a)


m = [
    [0, 1, 2],
    [1, 1, 2],
    [0, 1, 2]
]


print_m(m)
print_m(zero(m))