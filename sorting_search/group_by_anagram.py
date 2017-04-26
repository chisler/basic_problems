from collections import defaultdict


def group(a):
    h = defaultdict(list)
    for s in a:
        h[str(sorted(s))].append(s)

    res = []

    for v in h.values():
        for s in v:
            res.append(s)

    return res

a = ['abba', 'tata', 'baba', 'atta']

print(group(a))