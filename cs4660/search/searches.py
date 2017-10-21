"""
Searches module defines all different search algorithms
"""
import sys
sys.path.append("../")
from collections import deque
from graph.graph import Edge


def bfs(graph, initial_node, dest_node):
    """
    Breadth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    # structures to keep track of parent, distance, visitied, to be visited
    parents = {}
    distances = {}
    visited = []
    path_list = []
    d = deque()

    # initialize parents and distance
    parents[initial_node] = None
    distances[initial_node] = 0
    visited.append(initial_node)
    d.append(initial_node)

    # while deque is not empty look for noeds to visit
    while len(d) != 0:
        cur_n = d.popleft()
        # look for current node's neighbors
        for neighbor in graph.neighbors(cur_n):
            if neighbor not in visited:
                d.append(neighbor)
                visited.append(neighbor)
                # add currnet neighbor's distance and parant to respective dict's
                parents[neighbor] = cur_n
                distances[neighbor] = distances[cur_n] + graph.distance(cur_n, neighbor)

            # break if dest node has been visited
            if dest_node in visited:
                break
            """
            q = Queue.Queue()
            distance = {}
            parent = {}
            visited = []
            path = []

            parent[empty_room['id']] = None
            distance[empty_room['id']] = 0

            q.put(empty_room['id'])

            while q.qsize() > 0:
                cur_node = q.get()
                # check to see if all "nodes" were being put in
                # print cur_node
                cur_node_neighbors = get_state(cur_node)['neighbors']
                # check for neighbors and  add to appropaite lists
                for neighbors in cur_node_neighbors:
                    if neighbors['id'] not in visited:
                        visited.append(neighbors['id'])
                        parent[neighbors['id']] = cur_node
                        distance[neighbors['id']] = distance[cur_node]
            """
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
    pass

def a_star_search(graph, initial_node, dest_node):
    """
    A* Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
pass