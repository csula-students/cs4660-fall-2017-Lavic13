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
#from graph.graph import Edge
import json
import codecs
import Queue


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


def bfs(empty_room, dest_room ):
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
        for neighbors in cur_node_neighbors:
            if neighbors['id'] not in visited:
                visited.append(neighbors['id'])
                parent[neighbors['id']] = cur_node
                distance[neighbors['id']] = distance[cur_node] + \
                                    transition_state(cur_node,neighbors['id'])['event']['effect']
                q.put(neighbors['id'])
        if dest_room in visited:
            break

    while parent[dest_room['id']] is not None:
        cur = dest_room['id']
        par = parent[dest_room['id']]
        cur_name = cur['location']['name']
        cur_id = cur['id']
        par_name = par['location']['name']
        par_id = par['id']
        value = transition_state(par, cur)['event']['effect']
        path.append(par_name + par_id + " :" + cur_name + cur_id + " :" + value)
        dest_room['id'] = parent[dest_room['id']]

    return distance[dest_room['id']]


def Dijkstra(empty_room,dest_room):
    pass





if __name__ == "__main__":

    empty_room = get_state('7f3dc077574c013d98b2de8f735058b4')
    dark_room = get_state('f1f131f647621a4be7c71292e79613f9')
    bfsvalue = bfs(empty_room, dark_room)
    print bfsvalue

