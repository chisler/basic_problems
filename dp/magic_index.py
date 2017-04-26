def find(a):

    l, h = 0, len(a) - 1

    while l < h:

        m = (l + h) // 2

        if a[m] == m:
            return m

        if a[m] > m:
            h = m - 1
        elif a[m] < m:
            l = m + 1

    return -1

a = [-1, 0, 1, 4, 5, 6, 7, 8, 9]

# a = list(range(6))

print(find(a))