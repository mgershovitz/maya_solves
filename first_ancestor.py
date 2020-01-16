# Related blog post - https://algoritmim.co.il/2019/06/24/first-ancestor/

class Node(object):
    def __init__(self, val, parent):
        self.val = val
        self.parent = parent
        self.visited = False

    def __repr__(self):
        return self.val

def find_first_ancestor_recur(x, y):
    if x is not None and y is not None and x == y:
        return x
    next_nodes = []
    for node in [x, y]:
        if node is not None:
            if node.visited:
                return node
            else:
                node.visited = True
        next_nodes.append(node.parent)
    return find_first_ancestor_recur(next_nodes[0], next_nodes[1])

def find_first_ancestor(x, y):
    if x.parent is None or y.parent is None:
        return
    return find_first_ancestor_recur(x.parent, y.parent)

def run_tests():
    a = Node("A", None)
    assert find_first_ancestor(a, a) is None

    b = Node("B", a)
    c = Node("C", a)

    assert find_first_ancestor(b, c) == a

    d = Node("D", b)
    e = Node("E", d)
    f = Node("F", d)

    assert find_first_ancestor(b, c) == a
    assert find_first_ancestor(d, e) == b
    assert find_first_ancestor(f, e) == d
    assert find_first_ancestor(e, c) == a


if __name__ == '__main__':
    run_tests()