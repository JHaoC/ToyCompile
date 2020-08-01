from tree import Tree, Node

constdistance = 20

stack = {}

# only one line


def token(line):
    tokenlist = []
    level = 0
    isbranch, iswhile = False, False

    for i in line.split():
        if i == "(":
            level -= constdistance
            continue
        if i == ")":
            level += constdistance
            if isbranch:
                tokenlist.append(("if", 5 + level))
                isbranch = False
                continue
            if iswhile:
                tokenlist.append(("while", 5 + level))
                iswhile = False
                continue
            continue
        if i == "{":
            level -= constdistance
            continue
        if i == "}":
            level += constdistance
            continue

        if i in ["+", "-"]:  # math level two
            tokenlist.append((i, 2 + level))
            continue
        if i in ["*", "/"]:  # math level one
            tokenlist.append((i, 1 + level))
            continue
        if i in ["==", "!=", "<"]:  # comparision
            tokenlist.append((i, 3 + level))
            continue
        if i == "=":  # assign
            tokenlist.append((i, 4 + level))
            continue
        if i == "if":  # branch
            # tokenlist.append((i, 5 + level))
            isbranch = True
            continue
        if i == "while":  # while loop
            iswhile = True
            continue
        if i == "print":  # print
            tokenlist.append((i, 5 + level))
            continue
        if i == ";":  # print
            tokenlist.append((i, 6 + level))
            continue

        else:
            tokenlist.append((i, 0 + level))

    print(tokenlist)
    return tokenlist


def tokenScripts(lines):
    if not lines:
        return None
    tokenlist = []
    level = 0
    isbranch, iswhile = False, False
    for line in lines:
        for i in line.split():
            if i == "(":
                level -= constdistance
                continue
            if i == ")":
                level += constdistance
                if isbranch:
                    tokenlist.append(("if", 5 + level))
                    isbranch = False
                    continue
                if iswhile:
                    tokenlist.append(("while", 5 + level))
                    iswhile = False
                    continue
                continue
            if i == "{":
                level -= constdistance
                continue
            if i == "}":
                level += constdistance
                continue

            if i in ["+", "-"]:  # math level two
                tokenlist.append((i, 2 + level))
                continue
            if i in ["*", "/"]:  # math level one
                tokenlist.append((i, 1 + level))
                continue
            if i in ["==", "!=", "<"]:  # comparision
                tokenlist.append((i, 3 + level))
                continue
            if i == "=":  # assign
                tokenlist.append((i, 4 + level))
                continue
            if i == "if":  # branch
                # tokenlist.append((i, 5 + level))
                isbranch = True
                continue
            if i == "while":  # while loop
                iswhile = True
                continue
            if i == "print":  # print
                tokenlist.append((i, 5 + level))
                continue
            if i == ";":  # print
                tokenlist.append((i, 6 + level))
                continue
            else:
                tokenlist.append((i, 0 + level))

    # print(tokenlist)
    return tokenlist


def parse(line):
    res = Tree()
    for (c, t) in line:
        res.add(c, t)
    res.printTree()
    return res


def fetch(value):
    if not value:
        return None
    if type(value) == bool:
        return value
    if value in stack.keys():
        return stack[value]
    try:
        return float(value)
    except ValueError as identifier:
        return value


def excuteNode(node):
    if not node:
        return None
    if not node.left and not node.right:
        return node.value
    if node.value == ";":
        # val = fetch(excuteNode(node.left))
        # if val:
        #     print(val)
        # val = fetch(excuteNode(node.right))
        # if val:
        #     print(val)
        fetch(excuteNode(node.left))
        fetch(excuteNode(node.right))
        return None
    if node.value == "while":
        while fetch(excuteNode(node.left)):
            excuteNode(node.right)
        return None

    val1 = excuteNode(node.left)

    if node.value == "if":
        if fetch(val1):
            excuteNode(node.right)
        return None

    val2 = excuteNode(node.right)
    if node.value == "+":
        return fetch(val1) + fetch(val2)
    if node.value == "-":
        return fetch(val1) - fetch(val2)
    if node.value == "*":
        return fetch(val1) * fetch(val2)
    if node.value == "/":
        return fetch(val1) / fetch(val2)
    if node.value == "==":
        return fetch(val1) == fetch(val2)
    if node.value == "!=":
        return fetch(val1) != fetch(val2)
    if node.value == "<":
        return fetch(val1) < fetch(val2)
    if node.value == "=":
        stack[val1] = fetch(val2)
        return None
    if node.value == "print":
        print(fetch(val2))
        return None


def excute(scrips):
    tokens = tokenScripts(scrips)
    tree = parse(tokens)
    print("Result: " + str(excuteNode(tree.root)))


# def excute(line):
#     print("\n" + line)
#     tree = parse(line)
#     print("Result: " + str(excuteNode(tree.root)))

if __name__ == "__main__":
    # equ = "( ( 1 + 3 ) + 5 ) * 6 - 8 / 2"
    # excute(equ)
    # equ = "( 1 + 3 ) + 5 == 6 - 8 / 2"
    # excute(equ)
    equ = ["a = 10", "print ( a )"]
    tree = parse(tokenScripts(equ))
