"""
quiz2!

Use path finding algorithm to find your way through dark dungeon!

Technical detail wise, you will need to find path from node 7f3dc077574c013d98b2de8f735058b4
to f1f131f647621a4be7c71292e79613f9

TODO: implement BFS
TODO: implement Dijkstra utilizing the path with highest effect number
"""
import sys
sys.path.append('../')
from graph import graph
import json
import codecs
from collections import deque


# http lib import for Python 2 and 3: alternative 4
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

GET_STATE_URL = "http://192.241.218.106:9000/getState"
STATE_TRANSITION_URL = "http://192.241.218.106:9000/state"

def get_state(room_id):
    """
    get the room by its id and its neighbor
    """
    body = {'id': room_id}
    return __json_request(GET_STATE_URL, body)

def transition_state(room_id, next_room_id):
    """
    transition from one room to another to see event detail from one room to
    the other.

    You will be able to get the weight of edge between two rooms using this method
    """
    body = {'id': room_id, 'action': next_room_id}
    return __json_request(STATE_TRANSITION_URL, body)

def __json_request(target_url, body):
    """
    private helper method to send JSON request and parse response JSON
    """
    req = Request(target_url)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    reader = codecs.getreader("utf-8")
    response = json.load(reader(urlopen(req, jsondataasbytes)))
    return response


def bfs(graph, initial_node, dest_node):
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
                visited.append(neighbor)
                d.append(neighbor)
                # add currnet neighbor's distance and parant to respective dict's
                parents[neighbor] = cur_n
                distances[neighbor] = distances[cur_n] + graph.distance(cur_n, neighbor)

            # break if dest node has been visited
            if dest_node in visited:
                break

    # get the path of the dest_node back to start node
    while parents[dest_node] is not None:
        edge = Edge(parents[dest_node], dest_node, graph.distance(parents[dest_node], dest_node))
        path_list.append(edge)
        dest_node = parents[dest_node]

    path_list.reverse()
    return path_list




def dijkstra_search(graph, start_node, dest_node):
    parents = {}
    distances = {}
    d = deque()
    path = []
    visited = []

    parents[start_node] = None
    distances[start_node] = 0

    d.append(start_node)
    visited.append(start_node)
    #while len(d) != 0:
    #have not complted
if __name__ == "__main__":
    # Your code starts here
    empty_room = get_state('7f3dc077574c013d98b2de8f735058b4')
    print(empty_room)
    print(transition_state(empty_room['id'], empty_room['neighbors'][0]['id']))
