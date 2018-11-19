# -*- coding: utf-8 -*-
"""General Tree module.

*Warning:* All the functions defined in this module are assumed to receive a
non-None value for their ``ref`` parameter.

"""

from . import queue
from .queue import Queue


class TreeAsBin:
    """Simple class for general tree.

    General trees are here represented as binary trees using the
    "first child - right sibling" view.

    Attributes:
        key (Any): Node key.
        child (TreeAsBin): First child reference.
        sibling (TreeAsBin): First sibling reference.

    """

    def __init__(self, key, child=None, sibling=None):
        """Init general tree with first child and first sibling references.

        Args:
            key (Any).
            child (TreeAsBin).
            sibling (TreeAsBin).

        """

        self.key = key
        self.child = child
        self.sibling = sibling


def size(ref):
    """Compute size of tree.

    Args:
        ref (TreeAsBin).

    Returns:
        int: The number of nodes of tree.

    """

    s = 1
    child = ref.child
    while child:
        s += size(child)
        child = child.sibling
    return s


def sizebin(ref):
    """Compute size of tree.

    This is an alternate version using the binary structure of the tree.

    Args:
        ref (TreeAsBin).

    Returns:
        int: The number of nodes of tree.

    """

    if ref == None:
        return 0
    else:
        return 1 + sizebin(ref.child) + sizebin(ref.sibling)


def height(ref):
    """Compute height of tree.

    Args:
        ref (TreeAsBin).

    Returns:
        int: The maximum depth of any leaf.

    """

    h = -1
    child = ref.child
    while child:
        h = max(h, height(child))
        child = child.sibling
    return h + 1


def heightbin(ref):
    """Compute height of tree.

    This is an alternate version using the binary structure of the tree.

    Args:
        ref (TreeAsBin).

    Returns:
        int: The maximum depth of any leaf.

    """

    if ref == None:
        return -1
    else:
        return max(1 + heightbin(ref.child), heightbin(ref.sibling))


def epl(ref, h=0):
    """Compute external paths' length.

    Args:
        ref (TreeAsBin).
        h (int): Current height.

    Returns:
        int: The total length of paths from root to leaves.

    """

    if ref.child:
        length = 0
        child = ref.child
        while child:
            length += epl(child, h+1)
            child = child.sibling
        return length
    else:
        return h


def search(ref, val):
    """Search for a value in tree.

    Args:
        ref (TreeAsBin).
        val (Any): Value to search.

    Returns:
        Tree: First node containing key val.

    """

    if ref.key == val:
        return ref
    else:
        node = None
        if ref.child:
            node = search(ref.child, val)
        if not node and ref.sibling:
            node = search(ref.sibling, val)
        return node


def __loadtree(s, typelt, i=0):
    # Validate start character
    if i < len(s) and s[i] == '(':
        # Skip parenthesis and extract key
        i = i + 1
        word = ""
        while not (s[i] in "()"):
            word = word + s[i]
            i += 1
        T = TreeAsBin(typelt(word))
        # Extract first child
        T.child, i = __loadtree(s, typelt, i)
        # Pass the ')'
        i = i + 1
        # Extract first sibling
        T.sibling, i = __loadtree(s, typelt, i)
        return T, i
    else:
        return None, i


def loadtree(path, typelt=int):
    # Open file and get full content
    file = open(path, 'r')
    content = file.read()
    # Remove all whitespace characters for easier parsing
    content = content.replace('\n', '').replace('\r', '') \
                     .replace('\t', '').replace(' ', '')
    file.close()
    # Parse content and return tree
    (T, _) = __loadtree(content, typelt)
    return T


def dot(ref):
    """Write down dot format of tree.

    Args:
        ref (TreeAsBin).

    Returns:
        str: String storing dot format of tree.

    """

    s = "graph {\n"
    s += "node [shape=circle, fixedsize=true, height=0.5, width=0.5]\n"
    s += str(ref.key) + "\n"
    q = Queue()
    q.enqueue(ref)
    while not q.isempty():
        ref = q.dequeue()
        child = ref.child
        while child:
            s = s + "   " + str(ref.key) + " -- " + str(child.key) + "\n"
            q.enqueue(child)
            child = child.sibling
    s += "}"
    return s


def display(ref):
    """Render a tree.

    *Warning:* Made for use within IPython/Jupyter only.

    Args:
        ref (TreeAsBin).

    Returns:
        Source: Graphviz wrapper object for tree display.

    """

    # Ensure all modules are available
    try:
        from graphviz import Source
    except:
        raise Exception("Missing module: graphviz.")
    # Build dot and wrap
    return Source(dot(ref))
