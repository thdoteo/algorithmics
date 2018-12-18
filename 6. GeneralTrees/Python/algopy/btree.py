# -*- coding: utf-8 -*-
"""BTree Module.

BTree class definition and standard methods and functions.

*Warning:*  Set ``BTree.degree`` before any tree instanciation.

"""

from . import queue
from .queue import Queue


class BTree:
    """BTree class.

    Attributes:
        degree (int): Degree for all existing trees.
        keys (list[Any]): List of node keys.
        children (list[BTree]): lLst of children.

    """

    degree = None

    def __init__(self, keys=None, children=None):
        """BTree instance constructor.

        Args:
            keys (list[Any]).
            children (list[BTree])

        """
        self.keys = keys if keys else []
        self.children = children if children else []

    @property
    def nbkeys(self):
        """Number of keys in node.

        Returns:
            int.

        """
        return len(self.keys)

    def _repr_svg_(self):
        '''Generate SVG representation.

        Requires graphviz module.

        Returns:
            string (SVG)
        '''
        try:
            from graphviz import Source
        except:
            raise Exception('Missing module: graphviz')
        return Source(dot(self))._repr_svg_()

    def _display(self):
        '''Displays SVG representation directly in IPython notebook.

        Requires IPython and (through method _repr_svg_) graphviz modules.
        '''
        try:
            from IPython.display import display_svg
        except:
            raise Exception('Missing moduke: IPtyhon')
        display_svg(self)


def __isvalid(ref, inf, sup):
    """Auxiliary function for isvalid.

    Checks order of keys in BTree node and if all have values in
    between second and third arguments.

    Args:
        ref (BTree).
        inf (int): Lower interval bound for key values.
        sup (int): Upper interval bound for key values.

    Returns:
        bool.

    """

    if ref.keys[0] < inf or ref.keys[ref.nbkeys-1] > sup:
        return False
    else:
        for i in range(ref.nbkeys-1):
            if ref.keys[i] >= ref.keys[i+1]:
                return False
        if ref.children:
            for i in range(ref.nbkeys):
                if not __isvalid(ref.children[i], inf, ref.keys[i]):
                    return False
                inf = ref.keys[i]
            return __isvalid(ref.children[ref.nbkeys], inf, sup)
        else:
            return True


def isvalid(ref):
    """Checks if BTree object is has a valid BTree structure.

    Checks order of keys in BTree nodes.

    Args:
        ref (BTree).

    Returns:
        bool: True if BTree has valid strucutre False if not.

    """

    return ref is None or __isvalid(ref, -float('inf'), float('inf'))


def __node_dot(ref):
    """Gets node into dot proper shape.

    Args:
        ref (BTree).

    """

    s = str(id(ref)) + '[label="'
    for i in range(ref.nbkeys-1):
        s += str(ref.keys[i]) + ' | '
    s += str(ref.keys[ref.nbkeys-1])
    s +=  '"];\n'
    return s


def __link_dot(ref_a, ref_b):
    """Writes down link between two BTree nodes in dot format.

    Args:
        ref_A (BTree).
        ref_B (BTree).

    """

    return "   " + str(id(ref_a)) + " -- " + str(id(ref_b)) + ";\n"


def dot(ref):
    """Writes down dot format of tree.

    Args:
        ref (BTree).

    Returns:
        str: String storing dot format of BTree.

    """

    s = "graph " + str(ref.degree) + " {\n"
    s += "node [shape = record, height=.1];\n"
    q = Queue()
    q.enqueue(ref)
    s += __node_dot(ref)
    while not q.isempty():
        ref = q.dequeue()
        for child in ref.children:
            s += __node_dot(child)
            s += __link_dot(ref, child)
            q.enqueue(child)
    s += "}"
    return s

def __display(ref):
    try:
        from graphviz import Source
        from IPython.display import display_svg
    except:
        raise Exception('Missing module: graphviz and/or IPython')
    display_svg(Source(dot(ref)))

def display(ref, filename='temp'):
    """Render a BTree to SVG format.

    *Warning:* Made for use within IPython/Jupyter only.

    Args:
        ref (BTree).
        filename (str): Temporary filename to store SVG output.

    Returns:
        SVG: IPython SVG wrapper object for BTree.

    """

    # Ensure all modules are available
    try:
        from graphviz import Graph, Source
        from IPython.display import SVG
    except:
        raise Exception("Missing module: graphviz and/or IPython.")
    # Traverse Btree and generate temporary Graph object
    output_format = 'svg'
    graph = Graph(filename, format=output_format)
    q = Queue()
    if ref is not None:
        queue.enqueue(q, ref)
    while not queue.isEmpty(q):
        ref = queue.dequeue(q)

        node_label = ''
        for i in range(ref.nbkeys-1):
            node_label += str(ref.keys[i]) + ' | '
        node_label += str(ref.keys[ref.nbkeys - 1])
        graph.node(str(id(ref)), label=node_label,
                   style="rounded", shape="record")

        for child in ref.children:
            graph.edge(str(id(ref)), str(id(child)))
            queue.enqueue(q, child)
    # Render to temporary file and SVG object
    graph.render(filename=filename, cleanup=True)
    return SVG(filename + '.' + output_format)
