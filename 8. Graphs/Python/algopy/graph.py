# -*- coding: utf-8 -*-
"""Graph module.

Provide an implementation of graphs with adjacency lists.

In a graph, vertices are considered numbered from 0 to the order of the graph
minus one. The vertex key, or number, can then be used to access its
adjacency list.

"""


class Graph:
    """ Simple class for graph: adjacency lists

    Attributes:
        order (int): Number of vertices.
        directed (bool): True if the graph is directed. False otherwise.
        adjlists (List[List[int]]): Lists of connected vertices for each vertex.

    """

    def __init__(self, order, directed=False):
        """Init graph, allocate adjacency lists

        Args:
            order (int): Number of nodes.
            directed (bool): True if the graph is directed. False otherwise.

        """

        self.order = order
        self.directed = directed
        self.adjlists = []
        for _ in range(order):
            self.adjlists.append([])


    def addedge(self, src, dst):
        """Add egde to graph.
    
        Args:
            src (int): Source vertex.
            dst (int): Destination vertex.
    
        Raises:
            IndexError: If any vertex index is invalid.
            Exception: If graph is None.
    
        """
        # Check graph
        if self is None:
            raise Exception('Empty graph')
        if src >= self.order or src < 0:
            raise IndexError("Invalid src index")
        if dst >= self.order or dst < 0:
            raise IndexError("Invalid dst index")
        # Add edge and reverse-edge if undirected.
        self.adjlists[src].append(dst)
        if not self.directed and dst != src:
            self.adjlists[dst].append(src)


    def addvertex(self, number=1):
        """Add number vertices to graph.
    
        Args:
            ref (Graph).
            number (int): Number of vertices to add.
        Raises:
            Exception: If graph is None.
    
        """
        # Check graph
        if self is None:
            raise Exception('Empty graph')
        # Increment order and extend adjacency list
        self.order += number
        for _ in range(number):
            self.adjlists.append([])

def todot(G):
    """Dot format of graph.

    Args:
        Graph

    Returns:
        str: String storing dot format of graph.

    """
    (dot, link) = ("digraph {\n", "->") if G.directed else ("graph {\n", "--")
    # Going through vertices 
    for v in range(G.order):
        # Going though links of a v
        for s in G.adjlists[v]:
            if G.directed or s >= v:
                dot += "{} {} {}\n".format(v, link, s)
    dot += "}"
    return dot


def display(G, eng=None):
    """
    *Warning:* Made for use within IPython/Jupyter only.
    """
    
    try:
        from graphviz import Source
        from IPython.display import display
    except:
        raise Exception("Missing module: graphviz and/or IPython.")
    display(Source(todot(G), engine = eng))


# load / save gra format    

def loadgra(filename):
    """Build a new graph from a GRA file.

    Args:
        filename (str): File to load.

    Returns:
        Graph: New graph.

    Raises:
        FileNotFoundError: If file does not exist. 

    """
    f = open(filename)
    directed = bool(int(f.readline())) # readline strips \n
    order = int(f.readline())
    G = Graph(order, directed)
    for line in f.readlines():
        edge = line.strip().split(' ')
        G.addedge(int(edge[0]), int(edge[1]))
    f.close()
    return G


def savegra(G, fileOut):
    #FIXME
    pass
