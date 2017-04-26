def search(a, l, r, x):
    m = (l + r) // 2

    if a[m] == x:
        return m

    if r < l:
        return -1

    # Left is normally ordered
    if a[l] < a[m]:
        if a[l] <= x < a[m]:
            return search(a, l, m - 1, x)
        return search(a, m + 1, r, x)

    # Right is normally ordered
    if a[m] < a[l]:
        if a[m] < x <= a[r]:
            return search(a, m + 1, r, x)
        return search(a, l, m - 1, x)

    # Left or right half is all repeats
    if a[l] == a[m]:
        if a[m] != a[r]:
            return search(a, m + 1, r, x)
        res = search(a, l, m - 1, x)

        if res == -1:
            return search(a, m + 1 , r, x)
        return res

    return -1


a = [4, 5, 6, 1, 2, 3]
print(search(a, 0, len(a)-1, 5))