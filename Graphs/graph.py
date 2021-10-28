class Graph(object):
    def __init__(self, graph_dict=None) -> None:
        super().__init__()
        """ initializes a graph object 
        If no dictionary or None is given, 
        an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = ()
        self._graph_dict = graph_dict
    
    def edges(self,vertice):
        "returns a list of all edges of a vertice"
        return self._graph_dict[vertice]

    def all_vertices(self):
        "returns the vertices as a set"
        return set(self._graph_dict.keys())
    
    def all_edges(self):
        "returns all edges of a graph"
        return self.generate_edges()

    def add_vertex(self,vertex):
        if vertex not in self._graph_dict:
            self._graph_dict[vertex] = []
    
    def add_edge(self,edge):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        edge = set(edge)
        vertex1, vertex2 = tuple(edge)
        for x, y in [(vertex1,vertex2), (vertex2,vertex1)]:
            if x in self._graph_dict:
                self._graph_dict[x].add(y)
            else:
                self._graph_dict[x] = [y]

    def __generate_edged(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self._graph_dict:
            for neighbour in self._graph_dict[vertex]:
                if (neighbour,vertex) not in edges:
                    edges.append({vertex,neighbour})
        return edges

    