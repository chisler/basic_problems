from collections import defaultdict


def palindrome_perm(s):
    h = defaultdict(int)
    for c in s.lower():
        if 'a' <= c <= 'z':
            h[c] += 1
    odd = False

    for v in h.values():
        if v % 2 == 1:
            if not odd:
                odd = True
            else:
                return False
    return True

s = 'Tact Coa'


print(palindrome_perm(s))
