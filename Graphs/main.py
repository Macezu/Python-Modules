from graph import Graph

g = { "a" : {"c","b"},
      "b" : {"a","d"},
      "c" : {"a","d"},
      "e" : {"c"},
      "f" : {}  
    }

graph = Graph(g)

for vertice in graph:
    print(f"Edges of vertice {vertice}: ", graph.edges(vertice))

print("Add vertex:")
graph.add_vertex("z")

print("Add an edge:")
graph.add_edge({"a", "d"})

print("Vertices of graph:")
print(graph.all_vertices())

print("Edges of graph:")
print(graph.all_edges())