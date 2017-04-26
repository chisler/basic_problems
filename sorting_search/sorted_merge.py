def merge(a, b):
    rest = len(b)
    i, j = len(a) - rest - 1, rest - 1

    while i >= 0 and j >= 0:
        if a[i] > b[j]:
            a[i + j + 1] = a[i]
            i -= 1
        else:
            a[i+j + 1] = b[j]
            j -= 1

    return a

b = [1, 2, 5]
a = [0, 3, 6] + [0] * len(b)

print(merge(a, b))