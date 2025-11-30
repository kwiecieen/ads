class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None

def nastepnik(w):
    if w.right is not None:
        w = w.right
        while w.left is not None:
            w = w.left
        return w
    else:
        while w.parent is not None and w.parent.left != w:
            w = w.parent
        return w.parent

