from typing import List, Set, Tuple, Optional, Generator

import networkx as nx
import numpy as np

def generate_tvg(ws_nkp: Tuple[float, float, float]) -> Tuple[nx.Graph, np.ndarray]:

    # generate the original graph with given parameter
    base_graph = nx.generators.random_graphs.connected_watts_strogatz_graph(*ws_nkp)
    # size of the network
    net_size = ws_nkp[0]
    # average degree of the network
    deg = ws_nkp[1]
    # average changing times of edges
    avg_freq = 5
    array = np.random.exponential(scale=1, size=avg_freq)
    return base_graph, array


def check_connection(array, time):
    # Check if the connection state of an edge needs to be changed
    # Return true if change needed, false if stays same
    sorted_array = sorted(array)
    # Find the two indexes where time falls in between
    # Apply binary search
    left_index = 0
    right_index = len(sorted_array) - 1
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_value = sorted_array[mid_index]

        if mid_value == time:
            return mid_index, mid_index + 1
        elif mid_value < time:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    if right_index % 2 == 1:
        return False
    else:
        return True

def update_graph(graph, time_stamp, current_time) -> nx.Graph:
    if check_connection(time_stamp, current_time) is True:
        if graph.has_edge(1, 2):
            graph.remove_edge(1, 2)
            print("Edge removed")
        else:
            graph.add_edge(1, 2)
            print("Edge added")
    return graph
    
