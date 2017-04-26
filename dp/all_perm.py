computed = set()

def perms(s):
    if s in computed:
        return []

    if len(s) == 1:
        return [s]

    res = []

    for i in range(len(s)):
        without_i = s[0:i] + s[i+1:]
        for perm in perms(without_i):
            res.append(s[i] + perm)

    computed.add(s)
    return res

print(perms('aabc'))