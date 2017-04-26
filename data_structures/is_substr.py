def is_rotated(s1, s2):
    return s1 in (s2 + s2)


s1 = 'waterbottle'
s2 = 'erbottlewat'

print(is_rotated(s1, s2))