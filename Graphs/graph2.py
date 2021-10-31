from graph import Graph


class Graph2(Graph):

    def vertex_degree(self,vertex):
        """ The degree of a vertex is the number of edges connecting
        it, i.e. the number of adjacent vertices. Loops are counted 
        double, i.e. every occurence of vertex in the list 
        of adjacent vertices. """
        degree = len(self._graph_dict[vertex])
        if vertex in self._graph_dict[vertex]:
            degree +1
        return degree
    
    def find_isolated_vertices(self):
        "returns isolated vertices"
        graph = self._graph_dict
        isolated = []
        for vertex in graph:
            print(isolated,vertex)
            if not graph[vertex]:
                isolated += [vertex]
        return isolated

    def Delta(self):
        "the maximum degree of the vertices"
        max = 0
        for vertex in self._graph_dict:
            vertex_degree = self._graph_dict(vertex)
            if vertex_degree > max:
                max = vertex_degree
        return max
    
    def degree_sequence(self):
        "calculates degree sequence"
        seq = []
        for vertex in self._graph_dict:
            seq.append(self.vertex_degree(vertex))
        seq.sort(reverse=True)
        return tuple(seq)