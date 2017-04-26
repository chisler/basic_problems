def one_away(s1, s2):
    short = s1 if len(s2) > len(s1) else s2
    long = s2 if len(s2) > len(s1) else s1

    len_s, len_l = len(short), len(long)

    if abs(len_l - len_s) > 1:
        return False

    i, j = 0, 0
    found_diff = False

    while i < len_s and j < len_l:

        if short[i] != long[j]:
            if found_diff:
                return False
            found_diff = True

            if len_s == len_l:
                # replacing
                i += 1

        else:
            # matching
            i += 1

        # equal
        j += 1

    return True


s1 = 'pale'
s2 = 'pakl;e'

print(one_away(s1, s2))