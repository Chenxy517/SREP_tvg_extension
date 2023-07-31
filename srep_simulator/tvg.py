from typing import List, Set, Tuple, Optional, Generator

import networkx as nx
import numpy as np

def generate_tvg(ws_nkp: Tuple[float, float, float]) -> Tuple[nx.Graph, np.ndarray]:

    # generate the original graph with given parameter
    # base_graph = nx.generators.random_graphs.connected_watts_strogatz_graph(*ws_nkp)

    # size of the network
    graph = nx.Graph()
    net_size = ws_nkp[0]
    nodes = range(net_size)
    graph.add_nodes_from(nodes)
    # graph.add_edge(0, 1)
    # average degree of the network
    deg = ws_nkp[1]
    # stamp_arr = [
    #     np.array([20, 30, 140, 150]),
    #     np.array([40, 50, 120, 130]),
    #     np.array([60, 70, 100, 110]),
    #     np.array([80, 90])

    # ]

    stamp_arr = []
    array_size = 50
    mean_interval = 20
    for i in range (net_size - 1):
        array = np.cumsum(np.random.exponential(scale=mean_interval, size=array_size))
        array1 = array + 2
        combined_array = np.sort(np.concatenate((array, array1)))
        stamp_arr.append(combined_array)
        # stamp_arr.append(np.cumsum(np.random.exponential(scale=mean_interval, size=array_size)))
    
    return graph, stamp_arr


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
    n = len(graph.nodes)
    for i in  range(n - 1):
        if check_connection(time_stamp[i], current_time) is True:
            graph.add_edge(i, i + 1)
            if i + 1 not in graph.nodes[i]['data'].replicas:
                graph.nodes[i]['data'].replicas[i + 1] = {i}
            if i not in graph.nodes[i + 1]['data'].replicas:
                graph.nodes[i + 1]['data'].replicas[i] = {i + 1}
            print("Edge added: ", i, i + 1, "time: ", current_time)
        else:
            if graph.has_edge(i, i + 1):
                graph.remove_edge(i, i + 1)
                print("Edge removed: ", i, i + 1, "time: ", current_time)
    return graph
    
