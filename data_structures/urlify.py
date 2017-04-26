def urlify(s):
    res = ''
    last = None
    for c in s.strip():
        if not last == c:
            if c == ' ':
                res += '%20'
            else:
                res += c
        elif last != ' ':
            res += c

    return res

s = 'Mr John Smith   '


print(urlify(s))
