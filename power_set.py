def power(a):

    if len(a) == 1:
        return [a]

    subsets = []
    i = a.pop()

    for s in power(a):
        subsets.append(s)
        c = s.union({i})
        subsets.append(c)

    subsets.append({i})
    return subsets


a = {1, 2, 3}

print(power(a))