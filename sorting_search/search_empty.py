def search(a, x):
    l, h = 0, len(a) - 1

    while l <= h:

        m = (l + h) // 2

        if a[m] == '':
            right = m + 1
            left = m - 1

            while True:
                if left < l and right > h:
                    return -1
                if right <= h and a[right] != '':
                    m = right
                    break
                if left >= l and a[left] != '':
                    m = left
                    break

                right += 1
                left -= 1
        if a[m] == x:
            return m
        if a[m] < x:
            l = m + 1
        if a[m] > x:
            h = m - 1

    return -1


a = ["at", "", "", "", "ball", "c", "d", "", "dad", "U"]

print(search(a, "U"))