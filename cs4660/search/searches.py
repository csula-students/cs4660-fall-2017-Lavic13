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


def r_dfs(graph, c_n, vis, par):
    for neighbor in graph.neighbors(c_n):
        if neighbor not in vis:
            vis[neighbor] = True
            par[neighbor] = c_n
            r_dfs(graph, c_n, vis, par)


def dfs(graph, initial_node, dest_node):
    """
    Depth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    parents = {}
    visited = {}
    parents[initial_node] = None
    path_list = []
    r_dfs(graph, initial_node, visited, parents)

    while parents[dest_node] is not None:
        edge = Edge(parents[dest_node], dest_node, graph.distance(parents[dest_node], dest_node))
        path_list.append(edge)
        dest_node = parents[dest_node]

    path_list.reverse()
    return path_list



def dijkstra_search(graph, initial_node, dest_node):
    """
    Dijkstra Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    d = Queue.PriorityQueue()
    distances = {}
    parents = {}
    path_list = []

    parents[initial_node] = None
    distances[initial_node] = 0
    d.put((0, initial_node))

    while d:
        # get tuple
        node = d.get()
        # get the actual node
        cur_node = node[1]

    # begin looking for current node's nieghbor
    # unable to read from here, but can in BFS???
        for neighbors in graph.neighbors[cur_node]:
            a_dist = distances[cur_node] + graph.distance(cur_node, neighbors)
            if neighbors not in distances:
                distances[neighbors] = graph.distance(cur_node, neighbors)
                parents[neighbors] = cur_node
                d.put(distances[neighbors],neighbors)
                # check to see if current distance is greater
            elif a_dist < distances[neighbors]:
                distances[neighbors] = graph.distance(cur_node, neighbors)
                parents[neighbors] = cur_node
                d.put(distances[neighbors],neighbors)
            elif cur_node == dest_node:
                break

    while parents[dest_node] is not None:
        edge = Edge(parents[dest_node], dest_node, graph.distance(parents[dest_node], dest_node))
        path_list.append(edge)
        dest_node = parents[dest_node]

    path_list.reverse()
    return path_list

def a_star_search(graph, initial_node, dest_node):
    """
    A* Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    pass

"""
l = [(1, 2), (3, 4), (6, 7), (5, 10)]
x = l.pop()
print x
"""