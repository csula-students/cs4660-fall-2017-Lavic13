"""
graph module defines the knowledge representations files
A Graph has following methods:
* adjacent(node_1, node_2)
    - returns true if node_1 and node_2 are directly connected or false otherwise
* neighbors(node)
    - returns all nodes that is adjacency from node
* add_node(node)
    - adds a new node to its internal data structure.
    - returns true if the node is added and false if the node already exists
* remove_node
    - remove a node from its internal data structure
    - returns true if the node is removed and false if the node does not exist
* add_edge
    - adds a new edge to its internal data structure
    - returns true if the edge is added and false if the edge already existed
* remove_edge
    - remove an edge from its internal data structure
    - returns true if the edge is removed and false if the edge does not exist
"""

from io import open
from operator import itemgetter


def construct_graph_from_file(graph, file_path):
    """
    TODO: read content from file_path, then add nodes and edges to graph object
    note that grpah object will be either of AdjacencyList, AdjacencyMatrix or ObjectOriented
    In example, you will need to do something similar to following:
    1. add number of nodes to graph first (first line)
    2. for each following line (from second line to last line), add them as edge to graph
    3. return the graph
    """
    f = open(file_path, 'r')
    text = f.read()
    lines = text.split('\n')

    num_nodes = lines[0]
    for n in range(int(num_nodes)):
        graph.add_node(Node(n))

    for line in lines[1:]:
        if len(line) > 0:
            # parse edge, then add to graph
            parts = list(map(int, line.split(':')))
            n_edges = (Edge(Node(int(parts[0])), Node(int(parts[1])), int(parts[2])))
            graph.add_edge(n_edges)

    f.close()
    return graph


class Node(object):
    """Node represents basic unit of graph"""
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return 'Node({})'.format(self.data)

    def __repr__(self):
        return 'Node({})'.format(self.data)

    def __eq__(self, other_node):
        return self.data == other_node.data

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.data)


class Edge(object):
    """Edge represents basic unit of graph connecting between two edges"""
    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight

    def __str__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.from_node, self.to_node, self.weight)

    def __repr__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.from_node, self.to_node, self.weight)

    def __eq__(self, other_node):
        return self.from_node == other_node.from_node and self.to_node == other_node.to_node and self.weight == \
                                                                                                 other_node.weight

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.from_node, self.to_node, self.weight))


class AdjacencyList(object):
    """
    AdjacencyList is one of the graph representation which uses adjacency list to
    store nodes and edges
    """
    def __init__(self):
        # adjacencyList should be a dictionary of node to edges
        self.adjacency_list = {}

    def adjacent(self, node_1, node_2):
        for edge in self.adjacency_list[node_1]:
            if node_2 == edge.to_node:
                return True
        else:
            return False

    def neighbors(self, node):
        n_list = []
        for edge in self.adjacency_list[node]:
            n_list.append(edge.to_node)
        return n_list

    def add_node(self, node):
        if node in self.adjacency_list:
            return False
        else:
            self.adjacency_list[node] = []
            return True

    def remove_node(self, node):
        if node not in self.adjacency_list:
            return False
        else:
            self.adjacency_list.pop(node)
            for i in self.adjacency_list:
                for edge in self.adjacency_list[i]:
                    if node == edge.to_node:
                        self.adjacency_list[i].remove(edge)
            return True

    def add_edge(self, edge):
        if edge.from_node in self.adjacency_list and edge.to_node in self.adjacency_list:
            if edge not in self.adjacency_list[edge.from_node]:
                self.adjacency_list[edge.from_node].append(edge)
                return True
            else:
                return False
        else:
            return False

    def remove_edge(self, edge):
        if edge.from_node in self.adjacency_list and edge.to_node in self.adjacency_list:
            if edge in self.adjacency_list[edge.from_node]:
                self.adjacency_list[edge.from_node].remove(edge)
                return True
            else:
                return False
        else:
            return False

    def distance(self, node_1, node_2):
        if node_1 in self.adjacency_list:
            for edge in self.adjacency_list[node_1]:
                if edge.to_node == node_2:
                    return edge.weight
        return False


class AdjacencyMatrix(object):
    def __init__(self):
        # adjacency_matrix should be a two dimensions array of numbers that
        # represents how one node connects to another
        self.adjacency_matrix = []
        # in additional to the matrix, you will also need to store a list of Nodes
        # as separate list of nodes
        self.nodes = []

    def adjacent(self, node_1, node_2):
        if node_1 in self.nodes and node_2 in self.nodes:
            f_index = self.__get_node_index(node_1)
            t_index = self.__get_node_index(node_2)
            if self.adjacency_matrix[f_index][t_index] == 0:
                return False
            else:
                return True
        else:
            return False

    def neighbors(self, node):
            nl_list = []
            f_index = self.__get_node_index(node)
            i = 0
            for j in self.adjacency_matrix[f_index]:
                if j != 0:
                    nl_list.append(self.nodes[i])
                i += 1
            return nl_list

    def add_node(self, node):
        if node in self.nodes:
            return False
        else:
            if len(self.nodes) > 0:
                for i in range(len(self.nodes)):
                    self.adjacency_matrix[i].append(0)
            self.nodes.append(node)
            self.adjacency_matrix.append([0] * len(self.nodes))
            return True

    def remove_node(self, node):
        if node in self.nodes:
            t_index = self.__get_node_index(node)
            self.nodes.remove(node)
            del self.adjacency_matrix[t_index]
            for i in self.adjacency_matrix:
                del i[t_index]
            return True
        else:
            return False

    def add_edge(self, edge):
        if edge.from_node in self.nodes and edge.to_node in self.nodes:
            f_index = self.__get_node_index(edge.from_node)
            t_index = self.__get_node_index(edge.to_node)
            if self.adjacency_matrix[f_index][t_index] == 0:
                self.adjacency_matrix[f_index][t_index] = edge.weight
                return True
            else:
                return False
        else:
            return False

    def remove_edge(self, edge):
        if edge.from_node in self.nodes and edge.to_node in self.nodes:
            f_index = self.__get_node_index(edge.from_node)
            t_index = self.__get_node_index(edge.to_node)
            if self.adjacency_matrix[f_index][t_index] != 0:
                self.adjacency_matrix[f_index][t_index] = 0
                return True
            else:
                return False
        else:
            return False

    def distance(self, node_1, node_2):
        if node_1 in self.nodes and node_2 in self.nodes:
            f_index = self.__get_node_index(node_1)
            t_index = self.__get_node_index(node_2)
            if self.adjacency_matrix[f_index][t_index] == 0:
                return 0
            else:
                return self.adjacency_matrix[f_index][t_index]
        else:
            return 0

    def __get_node_index(self, node):
        """helper method to find node index"""
        return self.nodes.index(node)


class ObjectOriented(object):
    """ObjectOriented defines the edges and nodes as both list"""
    def __init__(self):
        # implement your own list of edges and nodes
        self.edges = []
        self.nodes = []

    def adjacent(self, node_1, node_2):
        for edge in self.edges:
            if edge.from_node == node_1 and edge.to_node == node_2:
                return True
        return False

    def neighbors(self, node):
        n_list = []
        for edge in self.edges:
            if edge.from_node == node:
                n_list.append(edge.to_node)
        return n_list

    def add_node(self, node):
        if node in self.nodes:
            return False
        else:
            self.nodes.append(node)
            return True

    def remove_node(self, node):
        if node in self.nodes:
            self.nodes.remove(node)
            for edge in self.edges:
                if edge.from_node == node or edge.to_node == node:
                    self.edges.remove(edge)
            return True
        else:
            return False

    def add_edge(self, edge):
        if edge.to_node in self.nodes and edge.from_node in self.nodes:
            if edge not in self.edges:
                self.edges.append(edge)
                return True
            else:
                return False
        else:
            return False

    def remove_edge(self, edge):
        if edge in self.edges:
            self.edges.remove(edge)
            return True
        else:
            return False

    def distance(self, node_1, node_2):
        if node_1 in self.nodes and node_2 in self.nodes:
            for edge in self.edges:
                if node_1 == edge.from_node and node_2 in edge.to_node:
                    return edge.weight
