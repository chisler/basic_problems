class Listy(list):
    def element_at(self, i):
        if i < 0:
            return -1
        try:
            return self[i]
        except IndexError:
            return -1


def find_size(a):
    i = 1

    while a.element_at(i) != -1:
        i *= 2

    return i


def binary_search(a, size, x):
    l, h = 0, size

    while l <= h:
        m = (l + h) // 2

        el = a.element_at(m)

        if el == x:
            return m

        if el == -1 or el > x:
            h = m - 1
        else:
            l = m + 1

    return -1


def search(a, x):
    size = find_size(a)
    return binary_search(a, size, x)


a = Listy([1, 2, 3, 4, 5])

print(search(a, 4))