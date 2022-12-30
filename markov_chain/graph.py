"""Markov Chain Graph implementation

based on:
    - https://github.com/kying18/graph-composer.git

inspired by:
    - https://www.freecodecamp.org/news/python-projects-for-beginners/#markov-chain-text-composer-python-project

skills:
    - graph theory(!!)

additions / modifications:
    - properties!
    - edges / weights are properties, not generated lists
    - __repr__
    - the _graph_ connects two vertices, a vertex on it's own has no method to connect.
      - edges only make sense in the context of a graph so the vertex _knows_ about the
        edges that connect it to other vertices, but the _graph_ does the connecting
    - adding an edge automatically incremenets (instead of the other way around)
    - allow adding an edge to include an optional weight (instead of always 1)

"""

import random

class Vertex(object):
    """Vertex Class

    Properties:
        _label: The label for the Vertex.
        _edges: The dictionary of connecting edges and weights
    """
    def __init__(self, label):
        """Initialize the object

        Args:
            label: The unique label for the vertex node
        """
        self._label = label
        self._edges = {}

    @property
    def label(self):
        return self._label

    @property
    def edges(self):
        return list(self._edges.keys())
    
    @property
    def weights(self):
        return list(self._edges.values())

    def __repr__(self):
        vertex = self.label + ' -> [\n'
        for (target,weight) in self._edges.items():
            vertex += f'\t( {target.label} = {weight} )\n'
        
        vertex += ']\n'
        return vertex
    
    def add_edge(self, vertex, weight=1):
        """Add a connection to another Vertex

        Args:
            vertex (Vertex): The connected vertex
            weight (int, optional): The weight(preference) of the connection. Defaults to 1.
        """
        self._edges[vertex] = self._edges.get(vertex,0) + weight

    def next_node(self):
        """Get a random connected node

        Returns:
            vertex: random, weighted, vertex from the connected vertices
        """
        return random.choices(self.edges,weights=self.weights)[0]

class Graph:
    """Graph object

    Properties:
    """
    def __init__(self):
        self._vertices = {}
    
    def __repr__(self):
        graph = ''
        for vertex in self._vertices.values():
            graph += f'{vertex}'

        return graph

    @property
    def vertices(self):
        return set(self._vertices.keys())

    @vertices.setter
    def vertices(self,vertex):
        if vertex not in self.vertices:
            self._vertices[vertex] = Vertex(vertex)
    
    def add_vertex(self,label):
        # add a new Vertex object with the label
        self.vertices = label
    
    def get_vertex(self,label):
        # if a vertex we're looking for isn't in the graph, add it
        if label not in self.vertices:
            self.add_vertex(label)
        
        # return the vertex object
        return self._vertices[label]
    
    def get_next_node(self, current_node:Vertex):
        return self._vertices[current_node.label].next_node()
    
    def connect_to(self,vertex1,vertex2,weight=1):
        self.get_vertex(vertex1).add_edge(vertex2,weight)
