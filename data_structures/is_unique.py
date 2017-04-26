from collections import Counter


def is_unique(s):
    # we can go by character 
    c = Counter(s)
    for v in c.values():
        if v > 1:
            return False

    return True


def is_unique(s):
    last = None
    for c in sorted(s):
        if c == last:
            return False
        last = c

    return True


s = '1234s'

print(is_unique(s))

