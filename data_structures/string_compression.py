def compress(s):

    last = None
    cnt = 0
    res = ''

    for c in s:
        if c == last:
            cnt += 1
        else:
            if last:
                res += '{}{}'.format(cnt, last)
            cnt = 1
        last = c
    res += '{}{}'.format(cnt, c)
    return res

s = 'aaabbbss'

print(compress(s))