from collections import Counter


def is_permutation(s1, s2):
    return sorted(s1) == sorted(s2)


def is_permutation(s1, s2):
    c1 = Counter(s1)

    for c in s2:
        try:
            c1[c] -= 1
            if c1[c] < 0:
                return False
        except KeyError:
            return False

    return True

s1 = 'asd'
s2 = 'sad'

print(is_permutation(s1, s2))