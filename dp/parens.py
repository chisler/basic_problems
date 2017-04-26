def wrap(n):

    def parens(opening, closing, opened=0, s=''):
        if not closing and not closing:
            print(s)
            return

        if opened and closing:
            parens(opening, closing-1, opened-1, s + ')')

        if opening:
            parens(opening-1, closing, opened+1, s + '(')

    parens(n, n)

wrap(3)