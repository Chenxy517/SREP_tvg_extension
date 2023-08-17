from typing import List, Set, Tuple, Optional, Generator

import networkx as nx
import numpy as np

def generate_tvg(ws_nkp: Tuple[float, float, float]) -> Tuple[nx.Graph, np.ndarray]:

    # generate the original graph with given parameter
    # base_graph = nx.generators.random_graphs.connected_watts_strogatz_graph(*ws_nkp)

    # size of the network
    # graph.add_edge(0, 1)
    # average degree of the network
    # deg = ws_nkp[1]
    # stamp_arr = [
    #     np.array([20, 30, 140, 150]),
    #     np.array([40, 50, 120, 130]),
    #     np.array([60, 70, 100, 110]),
    #     np.array([80, 90])

    # ]

    # stamp_arr = []
    # array_size = 50
    # mean_interval = 19
    # for i in range (net_size - 1):
    #     array = np.random.exponential(scale=mean_interval, size=array_size)
    #     full_arr = [array[0], array[0] + 1]
    #     for j in range(1, array_size):
    #         full_arr.append(full_arr[-1] + array[j])
    #         full_arr.append(full_arr[-1] + 1)
    #     stamp_arr.append(full_arr)
    #     # stamp_arr.append(np.cumsum(np.random.exponential(scale=mean_interval, size=array_size)))

    diameter = 5
    net_size = 100
    nodes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    edges = [(0, 4), (0, 10), (0, 8), (1, 7), (1, 14), (2, 14), (3, 12), (5, 9), (6, 12),
            (8, 9), (8, 12), (8, 17), (8, 14), (8, 19), (9, 11), (12, 13), (14, 15),
            (14, 18), (15, 16)]

    # Create the graph
    graph = nx.Graph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)

    prob_con = 0.05
    prob_discon = 1 - prob_con

    stamp_arr = []
    # for i in range (net_size - 1):
    #     bool_array = np.random.choice([True, False], size=1000, p=[prob_con, prob_discon])
    #     array = []
    #     for index in range(0, 1000):
    #         if bool_array[index]:
    #             array.append(index)
    #     stamp_arr.append(array)
    
    for edge in edges:
        bool_array = np.random.choice([True, False], size=1000, p=[prob_con, prob_discon])
        array = []
        for index in range(0, 1000):
            if bool_array[index]:
                array.append(index)
        stamp_arr[edge] = array 

    stamp_arr_test = [[2,8],[5,10]]
    
    return graph, stamp_arr


def check_connection_exp(array, time):
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

def check_connection(array, time):
    if time in array:
        return True
    else:
        return False


def update_graph(graph, time_stamp, current_time) -> nx.Graph:
    for edge, time_arr in  time_stamp.item:
        node1 = edge[0]
        node2 = edge[1]
        if check_connection(time_arr, current_time):
            graph.add_edge(node1, node2)
            if node2 not in graph.nodes[node1]['data'].replicas:
                graph.nodes[node1]['data'].replicas[node2] = {node1}
            if node1 not in graph.nodes[node2]['data'].replicas:
                graph.nodes[node2]['data'].replicas[node1] = {node2}
            # print("Edge added: ", i, i + 1, "time: ", current_time)
        else:
            if graph.has_edge(node1, node2):
                graph.remove_edge(node1, node2)
                # print("Edge removed: ", i, i + 1, "time: ", current_time)
    return graph
    

def generate_graph_with_diameter(diameter):
    graph = nx.random_tree(20)  # Generate a random tree with diameter + 1 nodes
    while nx.diameter(graph) != diameter:
        graph = nx.random_tree(20)
    
    return graph

# desired_diameter = 5  # Replace with the desired diameter
# graph = generate_graph_with_diameter(desired_diameter)

# print("Graph Nodes:", graph.nodes())
# print("Graph Edges:", graph.edges())
# print("Graph Diameter:", nx.diameter(graph))
