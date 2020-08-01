class Node:
    def __init__(self, content, contenttype):
        self.value = content
        # 0: nums
        # 1: first level(*, /)
        # 2: second level(+, -)
        # 3: third lever(==, !=, <)
        self.type = contenttype
        self.left = None
        self.right = None


def stringNodes(node, level=0):
    if not node:
        return None, 0
    res = []
    leftnode, lflevel = stringNodes(node.left, level + 1)

    rightnode, rtlevel = stringNodes(node.right, level + 1)

    res.append(leftnode)
    res.append(node.value)
    res.append(rightnode)
    return res, max(lflevel, rtlevel) + 1


def addhelp(rootnode, content, contenttype):
    if not rootnode:
        return Node(content, contenttype)
    if rootnode.type < contenttype:
        res = Node(content, contenttype)
        res.left = rootnode
        return res
    else:
        rootnode.right = addhelp(rootnode.right, content, contenttype)
        return rootnode


class Tree:
    def __init__(self):
        self.root = None

    def add(self, content, contenttype):
        self.root = addhelp(self.root, content, contenttype)

    def printTree(self):
        nodes, level = stringNodes(self.root)
        print(nodes)


if __name__ == "__main__":
    testlist = [("a", 0), ("*", 1), ("a", 0), ("+", 2),
                ("a", 0), ("*", 1), ("a", 0)]
    res = Tree()
    for (c, t) in testlist:
        res.add(c, t)
    res.printTree()
