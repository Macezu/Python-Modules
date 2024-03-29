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
        return self.__generate_edges()

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

    def __generate_edges(self):
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

    def __iter__(self):
        self._iter_obj = iter(self._graph_dict)
        return self._iter_obj
    
    def __next__(self):
        "allows us to iter over the vertices"
        return next(self._iter_obj)
    
    def __str__(self) -> str:
        res = "vertices: "
        for k in self._graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def find_path(self, start_vertex, end_vertex, path=None):
        "find a path from start to end in graph"
        if path == None:
            path = []
        graph = self._graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, end_vertex, path)
                if extended_path:
                    return extended_path
        return None
    
    def find_all_paths(self,start_vertex, end_vertex, path = []):
        "find all paths from start_vertex to end_vertex in graph"
        graph = self._graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex,end_vertex, path)
                for p in extended_paths:
                    paths.append(p)
        return paths
    

