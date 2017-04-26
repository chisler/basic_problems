def is_div(a):
    return not bool(a & 1)


def multiply(a, b):
    if b <= 1:
        return a

    if is_div(b):
        return multiply(a << 1, b >> 1)

    return a + multiply(a, b-1)


print(multiply(5, 40))