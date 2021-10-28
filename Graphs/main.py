from graph import Graph

g = { "a" : {"c","b"},
      "b" : {"a","d"},
      "c" : {"a","d"},
      "e" : {"c"},
      "f" : {}  
    }

graph = Graph(g)
