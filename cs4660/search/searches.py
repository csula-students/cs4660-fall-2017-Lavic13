"""
Searches module defines all different search algorithms
"""
import sys
sys.path.append("../")
import Queue
from graph import graph
from graph.graph import Edge


def bfs(graph, initial_node, dest_node):
    """
    Breadth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """

    parents = {}
    distances = {}
    path_list = []
    d = Queue.deque()

    # initialize parents and distance
    parents[initial_node] = None
    distances[initial_node] = 0
    d.append(initial_node)

    # while deque is not empty look for noeds to visit
    while len(d) > 0:
        cur_n = d.popleft()
        # look for current node's neighbors
        for neighbor in graph.neighbors(cur_n):
            if neighbor not in distances:
                d.append(neighbor)
                # add currnet neighbor's distance and parant to respective dict's
                parents[neighbor] = cur_n
                distances[neighbor] = distances[cur_n] + graph.distance(cur_n, neighbor)

            # break if dest node has been visited
            if dest_node in distances:
                break

    # get the path of the dest_node back to start node
    while parents[dest_node] is not None:
        edge = Edge(parents[dest_node], dest_node, graph.distance(parents[dest_node], dest_node))
        path_list.append(edge)
        dest_node = parents[dest_node]

    path_list.reverse()
    return path_list

def dfs(graph, initial_node, dest_node):
    """
    Depth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    pass

def dijkstra_search(graph, initial_node, dest_node):
    """
    Dijkstra Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    q = []
    distance = {}
    parent = {}
    visited = []
    path = []

    parent[initial_node] = None
    distance[initial_node] = 0
    q.append((0, initial_node))

    while len(q) > 0:
        node = q.pop()
        cur_node = node[1]

        cur_node_neighbors = graph.neighbors(cur_node)
        for neighbors in cur_node_neighbors:
            if neighbors not in distance:

            elif:

        q.sort()

def a_star_search(graph, initial_node, dest_node):
    """
    A* Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
pass