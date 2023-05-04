
import heapq

# create a nested dictionary that stores info about the graph
my_graph = {
    "A": {
        "distance": 0,
        "previous_node": None,
        "visited": True,
        "neighbors": {
            "B": 5,
            "D": 4
        }
    },
    "B": {
        "distance": 5,
        "previous_node": "A",
        "visited": True,
        "neighbors": {
            "A": 5,
            "C": 3,
            "E": 4
        }
    },
    "C": {
        "distance": 8,
        "previous_node": "B",
        "visited": True,
        "neighbors": {
            "B": 3,
            "F": 2
        }
    },
    "D": {
        "distance": 4,
        "previous_node": "A",
        "visited": True,
        "neighbors": {
            "A": 4,
            "E": 1
        }
    },
    "E": {
        "distance": 5,
        "previous_node": "D",
        "visited": True,
        "neighbors": {
            "B": 4,
            "D": 1,
            "F": 7
        }
    },
    "F": {
        "distance": 7,
        "previous_node": "E",
        "visited": True,
        "neighbors": {
            "C": 2,
            "E": 7
        }
    }
}

# inf_graph = {
#     "A": {
#         "distance": float("inf"),
#         "previous_node": None,
#         "visited": False,
#         "neighbors": {
#             "B": 5,
#             "D": 4
#         }
#     },
#     "B": {
#         "distance": float("inf"),
#         "previous_node": None,
#         "visited": False,
#         "neighbors": {
#             "A": 5,
#             "C": 3,
#             "E": 4
#         }
#     },

# describe the algorithm


def dijkstra(graph, start_node):
    # initialize distances to Infinity and previous nodes to None for all nodes, except start_node with distance 0
    for node in graph:
        graph[node]["distance"] = float("inf")
        graph[node]["previous_node"] = None
        graph[node]["visited"] = False

    # set distance from start_node to itself, which is, naturally, zero
    graph[start_node]["distance"] = 0

    # initialize priority queue that stores the info about start_node as a tuple
    p_queue = [(graph[start_node]["distance"], start_node)]
    # p_queue = [(5, "B")]
    heapq.heapify(p_queue)

    while p_queue:  # while priority queue is not empty
        # get the node with smallest tentative distance
        current_distance, current_node = heapq.heappop(p_queue)

        # is the value of "visited" for this node is False
        if not graph[current_node]["visited"]:
            # mark node as visited
            graph[current_node]["visited"] = True

            # update distances and previous nodes of neighbors
            for neighbor, weight in graph[current_node]["neighbors"].items():
                tentative_distance = current_distance + weight
                if tentative_distance < graph[neighbor]["distance"]:
                    graph[neighbor]["distance"] = tentative_distance
                    graph[neighbor]["previous_node"] = current_node
                    heapq.heappush(p_queue, (tentative_distance, neighbor))

    # return the distances and previous nodes for all nodes
    new_dict = {node: (graph[node]["distance"], graph[node]
                       ["previous_node"]) for node in graph}
    return new_dict


print(dijkstra(my_graph, "A"))
