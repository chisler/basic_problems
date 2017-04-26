from collections import deque


class BST(object):
    def __init__(self, root=None):
        self.root = root
        self.size = 0 if not root else 1

    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = Node(key, value)

        self.size += 1

    def _put(self, key, value, current_node):
        if key < current_node.key:

            if current_node.left:
                self._put(key, value, current_node.left)
            else:
                current_node.left = Node(key, value, parent=current_node)
        else:
            if current_node.right:
                self._put(key, value, current_node.right)
            else:
                current_node.right = Node(key, value, parent=current_node)

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:
            return self._get(key, self.root)
        else:
            return None

    def _get(self, key, node):
        if node is None:
            return None

        if key == node.key:
            return node

        if key < node.key:
            return self._get(key, node.left)

        return self._get(key, node.right)

    def __getitem__(self, key):
        return self.get(key)

    def delete(self, key):
        if self.size > 1:
            node_to_delete = self._get(key, self.root)
            if node_to_delete:
                self.remove(node_to_delete)
            else:
                raise KeyError('No such node')
        else:
            if self.size == 1 and self.root.key == key:
                self.root = None
                self.size = 0
            else:
                raise KeyError('No such node')

    def remove(self, node):
        if node.is_leaf:
            if node.is_right_child:
                node.parent.right = None
            else:
                node.parent.left = None
            return

        if len(node.children()) == 1:
            if node.is_right_child:
                node.parent.right = node.right if node.right else node.left
            else:
                node.parent.left = node.right if node.right else node.left
            return

        # has both children
        successor = node.get_successor()
        key, value = successor.key, successor.value
        self.delete(successor.key)
        node.key, node.value = key, value

    def traverse(self):
        if not self.root:
            return

        queue = deque()
        queue.append((self.root, 0))

        while queue:
            node, level = queue.popleft()
            level += 1
            print(node, level)
            for child in node.children():
                queue.append((child, level))



class Node(object):
    def __init__(self, key, value, parent=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def children(self):
        return [child for child in [self.left, self.right] if child is not None]

    def __str__(self):
        return "key = {}, value = {}".format(self.key, self.value)

    def get_minimum(self):
        node = self
        while node.left:
            node = node.left
        return node

    def get_successor(self):
        if self.right:
            return self.right.get_minimum()

        if self.parent:
            if not self.is_right_child:
                return self.parent

            self.parent.right = None
            res = self.parent.get_successor()
            self.parent.right = self
            return res

        return None

    @property
    def is_leaf(self):
        return not (self.left or self.right)

    @property
    def is_right_child(self):
        return self.parent.right == self


bst = BST()

bst.put(17, 17)
bst.put(5, 5)
bst.put(35, 35)
bst.put(2, 2)
bst.put(38, 38)
bst.put(29, 29)

bst.traverse()
print("\n")
bst.delete(35)
bst.traverse()
