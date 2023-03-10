#!/usr/bin/env python3
import math
from enum import Enum
from typing import Any, Optional, TextIO


# definice barev
class Colors(Enum):
    red = 1
    black = 2


class Node:
    """Trida Node slouzi k reprezentaci uzlu ve strome.

    Atributy:
        key     klic daneho uzlu
        color   muze nabyvat hodnoty 'red' a 'black'
        parent  reference na rodice uzlu
        left    reference na leveho potomka
        right   reference na praveho potomka
    """

    def __init__(self) -> None:
        self.key: Any = 0
        self.color: Colors = Colors.black
        self.parent: Optional[Node] = None
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class RedBlackTree:
    """Trida RedBlackTree slouzi k reprezentaci cerveno-cerneho
    vyhledavaciho stromu.

    Atributy:
        root    reference na korenovy uzel typu Node
    """

    def __init__(self) -> None:
        self.root: Optional[Node] = None


def rotate_left(tree: RedBlackTree, rotation_root: Node) -> None:
    """Vykona rotaci doleva kolem uzlu 'rotation_root' ve strome 'tree'."""
    right_child = rotation_root.right
    if right_child is None:
        return

    successor = right_child.left
    rotation_root.right = successor
    if successor is not None:
        successor.parent = rotation_root

    parent = rotation_root.parent

    if parent is not None:
        if parent.left == rotation_root:
            parent.left = right_child
        else:
            parent.right = right_child
    else:
        tree.root = right_child
    right_child.parent = parent
    right_child.left = rotation_root
    rotation_root.parent = right_child



def rotate_right(tree: RedBlackTree, rotation_root: Node) -> None:
    """Vykona rotaci doprava kolem uzlu 'rotation_root' ve strome 'tree'."""

    left_child = rotation_root.left

    if left_child is None:
        return

    rotation_root.left = left_child.right
    if rotation_root.left is not None:
        rotation_root.left.parent = rotation_root

    parent = rotation_root.parent

    if parent is not None:
        if parent.left == rotation_root:
            parent.left = left_child
        else:
            parent.right = left_child
    else:
        tree.root = left_child
    left_child.parent = parent
    left_child.right = rotation_root
    rotation_root.parent = left_child




def insert(tree: RedBlackTree, key: Any) -> None:
    """Vlozi novy uzel s klicem 'key' do stromu 'tree'. Operace zachova
    korektni cerveno-cerny strom.
    """
    node = Node()
    node.key = key
    node.color = Colors.red

    if tree.root is None:
        tree.root = node
        fix_tree(tree, tree.root)
        return

    next_node = tree.root
    while True:
        if key > next_node.key and next_node.right is not None:
            next_node = next_node.right
        elif key > next_node.key and next_node.right is None:
            next_node.right = node
            break
        elif key <= next_node.key and next_node.left is not None:
            next_node = next_node.left
        elif key <= next_node.key and next_node.left is None:
            next_node.left = node
            break
    node.parent = next_node
    fix_tree(tree, node)
    return


def fix_tree(tree: RedBlackTree, node: Node):
    # this is because we are inserting red node, so we are checking if we can stop, once the property is fine

    while node.parent is not None and node.parent.color == Colors.red:
        # this is for getting the uncle node
        if node.parent == node.parent.parent.left:
            uncle = node.parent.parent.right
            # case 1 this can only happen if there are more layers, so you can access the grandparent
            if uncle is not None and uncle.color == Colors.red:
                uncle.color = Colors.black
                node.parent.color = Colors.black
                node.parent.parent.color = Colors.red
                node = node.parent.parent
            else:
                if node == node.parent.right:
                    node = node.parent
                    rotate_left(tree, node)
                node.parent.color = Colors.black
                node.parent.parent.color = Colors.red
                rotate_right(tree, node.parent.parent)
        else:
            uncle = node.parent.parent.left
            if uncle is not None and uncle.color == Colors.red:
                uncle.color = Colors.black
                node.parent.color = Colors.black
                node.parent.parent.color = Colors.red
                node = node.parent.parent
            else:
                if node == node.parent.left:
                    node = node.parent
                    rotate_right(tree, node)
                node.parent.color = Colors.black
                node.parent.parent.color = Colors.red
                rotate_left(tree, node.parent.parent)
        if node.parent is None:
            break
    tree.root.color = Colors.black




def search(tree: RedBlackTree, key: Any) -> Optional[Node]:
    """Vyhleda uzel s klicem 'key' ve strome 'tree'. Vrati uzel
    s hledanym klicem. Pokud se klic 'key' v strome nenachazi vraci None.
    """
    pass


def is_correct_rb_tree(tree: RedBlackTree) -> bool:
    """Overi jestli je strom 'tree' korektni cerveno-cerny vyhledavaci
    strom. Pokud ano vraci True, jinak False.
    """
    if tree.root.color == Colors.red:
        return False
    if recursive_check(tree.root) != -1:
        return True


def recursive_check(node: Node) -> int:
    if node.color != Colors.red and node.color != Colors.black:
        return -1
    black = 0
    if node.color == Colors.black:
        black = 1
    if node.color == Colors.red:
        res = False
        if node.right is not None and node.right.color != Colors.black:
            res = True
        if node.left is not None and node.left.color != Colors.black:
            res = True
        if res:
            return -1

    if node.left is None and node.right is None:
        return 0 + black

    l = 0
    if node.left is not None:
        l = recursive_check(node.left)
        if l == -1:
            return -1

    r = 0
    if node.right is not None:
        r = recursive_check(node.right)
        if r == -1:
            return -1

    if l == r:
        return l + black
    return -1


# Dodatek k graphvizu:
# Graphviz je nastroj, ktery vam umozni vizualizaci datovych struktur,
# coz se hodi predevsim pro ladeni. Tento program generuje nekolik
# souboru neco.dot v mainu. Vygenerovane soubory nahrajte do online
# nastroje pro zobrazeni graphvizu:
# http://sandbox.kidstrythisathome.com/erdos/
# nebo http://www.webgraphviz.com/ - zvlada i vetsi grafy.
#
# Alternativne si muzete nainstalovat prekladac z jazyka dot do obrazku
# na svuj pocitac.
def make_graph(rbtree: RedBlackTree, filename: str) -> None:
    try:
        with open(filename, 'w') as dot_file:
            dot_file.write("digraph RBTree {\n")
            dot_file.write("node [style=filled];\n")
            make_graphviz(rbtree.root, dot_file)
            dot_file.write("}\n")
        print("Vykresleny strom najdete v souboru", filename)
    except Exception:
        print("Ve vykreslovani nastala chyba")


def make_graphviz(node: Optional[Node], dot_file: TextIO) -> None:
    if node is None:
        return

    if node.color == Colors.red:
        color = "color=red"
    else:
        color = "color=black,fontcolor=white"

    dot_file.write('"{}" [{},label="{}"]\n'.format(id(node), color, node.key))

    for child, side in (node.left, 'L'), (node.right, 'R'):
        if child is not None:
            dot_file.write('"{}" -> "{}"\n'.format(id(node), id(child)))
            make_graphviz(child, dot_file)
        else:
            dot_file.write('{nil} [label="",color=white]\n{node} -> {nil}\n'
                           .format(node=id(node), nil=side + str(id(node))))


def init_rb_tree() -> RedBlackTree:
    tree = RedBlackTree()

    nodes = [Node() for _ in range(7)]

    for i in range(7):
        nodes[i].key = i

    tree.root = nodes[3]

    tree.root.left = nodes[1]
    nodes[1].parent = tree.root
    nodes[1].color = Colors.red
    nodes[1].left = nodes[0]
    nodes[0].parent = nodes[1]
    nodes[1].right = nodes[2]
    nodes[2].parent = nodes[1]

    tree.root.right = nodes[5]
    nodes[5].parent = tree.root
    nodes[5].left = nodes[4]
    nodes[5].color = Colors.red
    nodes[4].parent = nodes[5]
    nodes[5].right = nodes[6]
    nodes[6].parent = nodes[5]

    return tree


def init_unbalanced_tree_right() -> RedBlackTree:
    tree = RedBlackTree()

    nodes = [Node() for _ in range(7)]

    tree.root = nodes[0]
    for i in range(7):
        nodes[i].key = i
    for i in range(1, 7):
        nodes[i].parent = nodes[i - 1]
    for i in range(6):
        nodes[i].right = nodes[i + 1]

    return tree


def init_unbalanced_tree_left() -> RedBlackTree:
    tree = RedBlackTree()

    nodes = [Node() for _ in range(7)]

    tree.root = nodes[6]
    for i in range(7):
        nodes[i].key = i
    for i in range(6):
        nodes[i].parent = nodes[i + 1]
    for i in range(1, 7):
        nodes[i].left = nodes[i - 1]

    return tree


def helper_test_rotate_left(tree: RedBlackTree) -> bool:
    assert tree.root
    rotate_left(tree, tree.root)

    assert tree.root.right
    if (tree.root.key != 1 or
            tree.root.left is None or
            tree.root.left.key != 0 or
            tree.root.right.key != 2):
        print("NOK - chybna rotace kolem korene stromu")
        return False

    rnode = tree.root.right
    rotate_left(tree, rnode)

    assert tree.root.right.right
    if (tree.root.right.key != 3 or
            tree.root.right.left is None or
            tree.root.right.left.right is not None or
            tree.root.right.left.key != 2 or
            tree.root.right.right.key != 4):
        print("NOK - chybna rotace kolem uzlu stromu")
        return False

    rnode = tree.root.left
    rotate_left(tree, rnode)

    if (rnode.left is not None or
            rnode.right is not None or
            tree.root.key != 1 or
            tree.root.left.key != 0):
        print("NOK - chybna rotace kolem uzlu bez potomka")
        return False

    rotate_left(tree, tree.root)

    assert tree.root.left.right
    if (tree.root.key != 3 or
            tree.root.right.key != 4 or
            tree.root.left.key != 1 or
            tree.root.left.right.key != 2):
        print("NOK - chybna rotace kolem korene stromu,",
              "testovani preveseni potomka")
        return False

    print("OK")
    return True


def test_rotate_left() -> None:
    print("Test 1. rotate_left: ")
    tree = init_unbalanced_tree_right()

    if not helper_test_rotate_left(tree):
        make_graph(tree, "rotate_left.dot")


def helper_test_rotate_right(tree: RedBlackTree) -> bool:
    assert tree.root
    rotate_right(tree, tree.root)

    assert tree.root.left
    if (tree.root.key != 5 or
            tree.root.right is None or
            tree.root.right.key != 6 or
            tree.root.left.key != 4):
        print("NOK - chybna rotace kolem korene stromu")
        return False

    rnode = tree.root.left
    rotate_right(tree, rnode)

    assert tree.root.left.left
    if (tree.root.left.key != 3 or
            tree.root.left.right is None or
            tree.root.left.right.left is not None or
            tree.root.left.left.key != 2):
        print("NOK - chybna rotace kolem uzlu stromu")
        return False

    rnode = tree.root.right
    rotate_right(tree, rnode)

    if (tree.root.right.left is not None or
            tree.root.right.right is not None or
            tree.root.key != 5 or
            tree.root.right.key != 6):
        print("NOK - chybna rotace kolem uzlu bez potomka")
        return False

    rotate_right(tree, tree.root)

    assert tree.root.right.left
    if (tree.root.key != 3 or
            tree.root.left.key != 2 or
            tree.root.right.key != 5 or
            tree.root.right.left.key != 4):
        print("NOK - chybna rotace kolem korene stromu, ",
              "testovani preveseni potomka")
        return False

    print("OK")
    return True


def test_rotate_right() -> None:
    print("Test 2. rotate_right: ")
    tree = init_unbalanced_tree_left()

    if not helper_test_rotate_right(tree):
        make_graph(tree, "rotate_right.dot")


def helper_test_insert(tree: RedBlackTree) -> bool:
    insert(tree, 5)

    if tree.root is None or tree.root.color != Colors.black:
        print("NOK - koren je cerveny")
        return False

    insert(tree, 9)

    if (tree.root.right is None or
            tree.root.right.color != Colors.red or
            tree.root.right.key != 9):
        print("NOK - chybne vlozeny cerveny uzel")
        return False

    insert(tree, 3)
    insert(tree, 4)

    assert tree.root.left and tree.root.left.right
    if (tree.root.color != Colors.black or
            tree.root.right.color != Colors.black or
            tree.root.left.color != Colors.black or
            tree.root.left.right.color != Colors.red or
            tree.root.left.right.key != 4):
        print("NOK - chybne prebarveni a vkladani")
        return False

    insert(tree, 6)
    insert(tree, 7)

    assert tree.root.right.left and tree.root.right.right
    if (tree.root.right.key != 7 or
            tree.root.right.left.key != 6 or
            tree.root.right.right.key != 9 or
            tree.root.right.color != Colors.black or
            tree.root.right.left.color != Colors.red or
            tree.root.right.right.color != Colors.red):
        print("NOK - chybna rotace vpravo s prebarvenim")
        return False

    insert(tree, 10)
    tnode = tree.root.right

    assert tnode.left and tnode.right and tnode.right.right
    if (tnode.color != Colors.red or
            tnode.left.color != Colors.black or
            tnode.right.color != Colors.black or
            tnode.right.right.color != Colors.red or
            tnode.right.right.key != 10):
        print("NOK - chybne prebarveni bez rotace")
        return False

    insert(tree, 8)
    insert(tree, 12)
    root = tree.root

    assert (
            root.left and root.left.right and
            root.right and root.right.left and root.right.right and
            root.right.right.right
    )
    if (root.key != 7 or
            root.left.key != 5 or
            root.left.right.key != 6 or
            root.right.left.key != 8 or
            root.right.right.right.key != 12 or
            root.color != Colors.black or
            root.left.color != Colors.red or
            root.right.color != Colors.red or
            root.left.right.color != Colors.black or
            root.right.left.color != Colors.black or
            root.right.right.right.color != Colors.red):
        print("NOK - chybna rotace kolem korene s prebarvenim")
        return False

    print("OK")
    return True


def test_insert() -> None:
    print("Test 3. insert: ")

    tree = RedBlackTree()

    if not helper_test_insert(tree):
        make_graph(tree, "insert.dot")


def helper_test_search(tree: RedBlackTree) -> bool:
    node = search(tree, 3)

    if node is None or node.key != 3:
        print("NOK - chybne hledani korene s hodnotou 3")
        return False

    node = search(tree, 2)

    if node is None or node.key != 2:
        print("NOK - chybne hledani listu s hodnotou 2")
        return False

    node = search(tree, 7)

    if node is not None:
        print("NOK - hledani prvku, ktery se v strome nevyskytuje")
        return False

    print("OK")
    return True


def test_search() -> None:
    print("Test 4. search: ")

    tree = init_rb_tree()

    if not helper_test_search(tree):
        make_graph(tree, "search.dot")


def helper_test_is_correct_rb_tree_1(tree: RedBlackTree) -> bool:
    if not is_correct_rb_tree(tree):
        print("NOK - strom je korektni")
        return False

    assert tree.root
    tree.root.color = Colors.red

    if is_correct_rb_tree(tree):
        print("NOK - strom ma cerveny koren")
        return False

    assert tree.root.left
    tree.root.color = Colors.black
    tree.root.left.color = Colors.black

    if is_correct_rb_tree(tree):
        print("NOK - strom nema stejnou cernou hloubku")
        return False

    return True


def helper_test_is_correct_rb_tree_2(tree: RedBlackTree) -> bool:
    if not is_correct_rb_tree(tree):
        print("NOK - strom je korektni")
        return False

    assert tree.root
    node = Node()
    node.key = 0
    node.parent = tree.root
    tree.root.left = node

    if is_correct_rb_tree(tree):
        print("NOK - strom nema stejnou cernou hloubku")
        return False

    tree.root.left.color = Colors.red

    if not is_correct_rb_tree(tree):
        print("NOK - strom je korektni")
        return False

    print("OK")
    return True


def test_is_correct_rb_tree() -> None:
    print("Test 5. is_correct_rb_tree: ")

    tree = init_rb_tree()

    if not helper_test_is_correct_rb_tree_1(tree):
        make_graph(tree, "correct.dot")
        return

    tree = RedBlackTree()
    tree.root = Node()
    tree.root.key = 1

    if not helper_test_is_correct_rb_tree_2(tree):
        make_graph(tree, "correct.dot")


if __name__ == '__main__':
    test_rotate_left()
    test_rotate_right()
    test_insert()
    test_search()
    test_is_correct_rb_tree()