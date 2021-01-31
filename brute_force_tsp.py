import itertools
import networkx as nx
import timeit

# brute force tsp function - O(n!)
def tsp(G, src_node, n):

    # store all nodes except source node
    nodes = []
    for i in range(n):
        if i != src_node:
            nodes.append(i)

    iterations = 0

    min_route = 1000000 #minimum route visiting all nodes
    node_permutation = itertools.permutations(nodes) #permutation of all edges

    for possible_route in node_permutation: #for permutation of nodes (possible routes)

        # total distance of current route
        route_dist = 0

        # sum of edge distances in route (total cost)
        departure_node = src_node
        for arrival_node in possible_route:
            route_dist += G[departure_node][arrival_node]['weight']
            departure_node = arrival_node
        route_dist += G[departure_node][src_node]['weight']

        # check if current route is the lowest so far
        min_route = min(min_route, route_dist)

        iterations += 1

    return min_route, iterations

if __name__ == "__main__":

    G = nx.Graph()

    G.add_weighted_edges_from([
        (0, 1, 2230),
        (0, 2, 1631),
        (0, 3, 1566),
        (0, 4, 1346),
        (0, 5, 1352),
        (0, 6, 1204),
        (0, 7, 1346),
        (0, 8, 1786),
        (0, 9, 1244),
        (1, 2, 845),
        (1, 3, 707),
        (1, 4, 1001),
        (1, 5, 947),
        (1, 6, 1484),
        (1, 7, 302),
        (1, 8, 266),
        (1, 9, 1320),
        (2, 3, 627),
        (2, 4, 773),
        (2, 5, 424),
        (2, 6, 644),
        (2, 7, 233),
        (2, 8, 1403),
        (2, 9, 685),
        (3, 4, 302),
        (3, 5, 341),
        (3, 6, 1027),
        (3, 7, 876),
        (3, 8, 1200),
        (3, 9, 1302),
        (4, 5, 368),
        (4, 6, 916),
        (4, 7, 656),
        (4, 8, 388),
        (4, 9, 876),
        (5, 6, 702),
        (5, 7, 344),
        (5, 8, 787),
        (5, 9, 989),
        (6, 7, 563),
        (6, 8, 1034),
        (6, 9, 244),
        (7, 8, 876),
        (7, 9, 454),
        (8, 9, 300),
    ])

    src_node = 0

    start = timeit.default_timer()

    print(tsp(G, src_node, 10))

    stop = timeit.default_timer()

    print('Run Time: ', stop - start) #print runtime of tsp implementation
