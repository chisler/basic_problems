def rotate(m):
    return list(map(lambda a: list(a), zip(*m)))


def print_m(m):
    for a in m:
        print(a)


m = [
    [0, 1, 2],
    [0, 1, 2],
    [0, 1, 2]
]

print_m(m)



print_m(rotate(m))