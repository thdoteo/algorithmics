# -*- coding: utf-8 -*-
"""Binary Tree module"""

from .queue import Queue


class BinTree:
    """Simple class for binary tree

    Attributes:
        key (Any): Node key.
        left (BinTree): Left child.
        right (BinTree): Right child.

    """

    def __init__(self, key, left, right):
        """Init binary tree.

        Args:
            key (Any): Node key.
            left (BinTree): Left child.
            right (BinTree): Right child.

        """

        self.key = key
        self.left = left
        self.right = right


def size(ref):
    """Compute size of tree.

    Args:
        ref (BinTree).

    Returns:
        int: The number of nodes of tree.

    """

    if ref == None:
        return 0
    else:
        return 1 + size(ref.left) + size(ref.right)


def height(ref):
    """Compute height of Tree.

    Args:
        ref (BinTree).

    Returns:
        int: The maximum depth of any leaf.

    """

    if ref == None:
        return -1
    else:
        return 1 + max(height(ref.left), height(ref.right))


def __epl(ref, h=0):
    """Auxiliary function for tree external path length.

    Args:
        ref (BinTree).
        h (int).

    Returns:
        (int, int): EPL, leaf count.

    """

    if ref == None:
        return (0, 0)
    elif ref.left == None and ref.right == None:
        return (h, 1)
    else:
        (lleft, nleft) = __epl(ref.left, h + 1)
        (lright, nright) = __epl(ref.right, h + 1)
        return (lleft + lright, nleft + nright)

def epl(ref):
    """Computes external path lenght of tree.

    Args:
        ref (BinTree).

    Returs:
        int.

    """

    return __epl(ref)[0]


def ead(ref):
    """Binary Tree External Average Depth.

    Args:
        ref (BinTree).

    Returns:
        float.

    """

    if ref == None:
        raise Exception("Empty tree.")
    else:
        (plength, nleaves) = __epl(ref)
        return plength / nleaves


def isdegenerate(ref):
    """Checks whether tree is degenerate.

    Args:
        ref (BinTree).

    Returns:
        bool.

    """

    if ref is None:
        return True
    else:
        if ref.left != None and ref.right != None:
            return False
        else:
            if ref.left != None:
                return isdegenerate(ref.left)
            else:
                return isdegenerate(ref.right)


def isperfect(ref):
    """Checks whether tree is perfect.

    Args:
        ref (BinTree).

    Returns:
        bool.

    """

    q = Queue()  # Stands for current level
    r = Queue()  # Stands for next level
    size_level = 0
    size_nextlevel = 0
    perfect = True

    if ref != None:
        q.enqueue(ref)

    while perfect and not q.isempty():
        node = q.dequeue()  # Count current level when dequeuing q
        size_level += 1

        if node.left != None:
            r.enqueue(node.left)  # Count next level when queueing r
            size_nextlevel += 1
        if node.right != None:
            r.enqueue(node.right)
            size_nextlevel += 1

        if q.isempty():
            if not r.isempty():
                # Check if next level twice as big as current
                perfect = (size_nextlevel == 2 * size_level)

            size_level = 0
            size_nextlevel = 0
            q = r
            r = Queue()

    return perfect


def iscomplete(ref):
    """Checks whether tree is complete.

    Args:
        ref (BinTree).

    Returns:
        bool.

    """

    complete = True
    level_start = True
    end_of_leaves = False  # Check we've got no leaves on the right of last level

    q = Queue()
    r = Queue()
    if ref != None:
        q.enqueue(ref)

    while complete and not q.isempty():
        node = q.dequeue()

        if node.left != None:
            if r.isempty() or end_of_leaves:
                # Ugly: make sure we didn't start a new level after end_of_leaves signal.
                complete = level_start and not end_of_leaves

            r.enqueue(node.left)
        else:
            end_of_leaves = True

        level_start = False

        if node.right != None:
            if r.isempty() or end_of_leaves:
                complete = False
            r.enqueue(node.right)
        else:
            end_of_leaves = True

        if q.isempty():
            q = r
            r = Queue()
            level_start = True

    return complete


def dot_simple(ref):
    """Writes down dot format of binary tree.

    This is a simple implementation for quick demo and understanding.

    Args:
        ref (BinTree).

    Returns:
        str: String storing dot format of BinTree.

    """

    s = "graph {\n" + 'graph [ordering="out"]\n'
    q = Queue()
    if ref:
        q.enqueue(ref)
    while not q.isempty():
        node = q.dequeue()
        if node.left:
            s += "   " + str(node.key) + " -- " + str(node.left.key) + "\n"
            q.enqueue(node.left)
        if node.right:
            s += "   " + str(node.key) + " -- " + str(node.right.key) + "\n"
            q.enqueue(node.right)
    s += "}"
    return s


def _dot_build_matrix(tree_height):
    """Build an empty matrix for BinTree node spreading.

    Resulting matrix will be of dimension:
    - (2 ** tree_height) lines
    - (tree_height) columns
    Tree is stored as if drawn from left to right. This allows simpler matrix
    reduction in the next step.

    Args:
        tree_height (int): BinTree height.

    Returns:
        List[List[None]]: Empty matrix.

    """

    matrix = []
    for _ in range(2 ** (tree_height + 1)):
        row = []
        for _ in range(tree_height + 1):
            row.append(None)
        matrix.append(row)
    return matrix


def _dot_reduce_matrix(matrix):
    """Remove empty columns from given matrix.

    One empty column is kept when possible.

    Args:
        matrix (List[List[str]]): BinTree node keys spread as if on grid paper.

    Returns:
        List[List[str]]: Deep copy of `matrix`, excluding empty columns.

    """

    reduced_matrix = []
    empty_column_added = True
    j = 0
    while j < len(matrix):
        row = matrix[j]
        i = 0
        while i < len(matrix[0]) and matrix[j][i] == None:
            i += 1
        # Keep non-empty columns
        if i < len(matrix[0]):
            reduced_matrix.append(row)
            empty_column_added = False
        # Keep first empty columns for visual appeal
        elif empty_column_added == False:
            reduced_matrix.append(row)
            empty_column_added = True
        j += 1
    # Return reduced matrix in place of initial matrix
    return reduced_matrix

def _dot_from_content(content, zoom_factor):
    """Produce final dot source from body lines.

    Args:
        content (List[str]): Lines to add to dot output.

    Returns:
        str: Full dot for BinTree.

    """

    zoom_factor /= 2.0
    res = """graph G {{
        layout="neato";
        node [shape=circle, fixedsize=true, height={z}, width={z}];
        edge [arrowhead=none];""".format(z=zoom_factor)
    for line in content:
        res += '\n        ' + line
    res += '\n}'
    return res

def dot(ref, wide_spread=False, zoom_factor=1.0,
             width_factor=1.0, height_factor=1.0):
    """Writes down dot format of binary tree.

    This is a "matrix" implementation used to spread nodes more evenly.
    It relies on a grid (``List[List[Tuple(BinTree, BinTree)]]``) and can
    put pressure on memory when tree gets high.

    Args:
        ref (BinTree).
        wide_spread (bool): Display whole tree width. Can get huge.
        zoom_factor (float): Multiplier for all dimensions and node size.
        width_factor (float): Multiplier for horizontal spacing.
        height_factor (float): Multiplier for vertical spacing.

    Returns:
        str: String storing dot format of BinTree.

    """

    # Container for graph dot source
    graph_content = []
    # Traversal
    if ref:
        # Compute tree height
        tree_height = height(ref)
        # Init queue, and fill node list with:
        #  - node and parent references
        #  - hirearchical and level numbers
        q = Queue()
        q.enqueue((ref, None, 1, 1))
        nodes = []
        while not q.isempty():
            node, parent, hier, level = q.dequeue()
            nodes.append((node, parent, hier, level))
            if None != node.left:
                q.enqueue((node.left, node, 2 * hier, level + 1))
            if None != node.right:
                q.enqueue((node.right, node, 2 * hier + 1, level + 1))
        # Prepare matrix to spread nodes evenly as if on grid paper
        node_matrix = _dot_build_matrix(tree_height)
        # Put nodes in their corresponding matrix cell depending on node's
        # level and hierarchical number.
        for node, parent, hier, level in nodes:
            # Get node rank in level from hierarchical number
            rank = (hier - 2 ** (level - 1))
            # Compute level's first node horizontal offset and inter-node space
            offset = 2 ** (tree_height - level + 1) - 1
            sep_pow = tree_height - level + 2
            sep = 2 ** sep_pow
            # Node coordinates in matrix space
            x = offset + (rank) * (sep)
            y = -level
            # Fill matrix with node/parent tuple to display link later
            node_matrix[x][y] = (node, parent)
        # Reduce matrix by removing empty columns for more compact display
        if not wide_spread:
            node_matrix = _dot_reduce_matrix(node_matrix)
        # Add graph content from node matrix
        for i in range(len(node_matrix)):
            for j in range(len(node_matrix[0])):
                if None != node_matrix[i][j]:
                    node, parent = node_matrix[i][j]
                    x = i * 0.25 * zoom_factor * width_factor
                    y = j / 1.5 * zoom_factor * height_factor
                    node_dot = 'N{}[label="{}";pos="{},{}!"];'
                    node_dot = node_dot.format(id(node), node.key, x, y)
                    graph_content.append(node_dot)
                    if None != parent:
                        edge_dot = 'N{} -- N{};'.format(id(parent), id(node))
                        graph_content.append(edge_dot)
    # Build graph and return
    return _dot_from_content(graph_content, zoom_factor=zoom_factor)


def display(ref, *args, **kwargs):
    """Render a BinTree to for in-browser display.

    *Warning:* Made for use within IPython/Jupyter only.

    Extra non-documented arguments are passed to the ``dot`` function and
    complyt with its documentation.

    Args:
        ref (BinTree).

    Returns:
        Source: Graphviz wrapper object for BinTree rendering.

    """

    # Ensure all modules are available
    try:
        from graphviz import Source
    except:
        raise Exception("Missing module: graphviz.")
    # Generate dot and return display object
    dot_source = dot(ref, *args, **kwargs)
    return Source(dot_source)
