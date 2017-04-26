class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minimal_tree(array, l=0, h=None):
    if h is None:
        h = len(array) - 1

    if l > h:
        return None

    m = (h + l) // 2

    node = TreeNode(a[m])

    node.left = minimal_tree(array, l, m - 1)
    node.right = minimal_tree(array, m + 1, h)

    return node



