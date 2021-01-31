# Copyright 2020 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License

## ------- import packages -------
import networkx as nx
import dimod
from dwave_networkx.utils import binary_quadratic_model_sampler
from collections import defaultdict
import itertools
from dwave.system import LeapHybridSampler
import timeit

def get_token():
    '''Return your personal access token'''

    token = 'DEV-b6dfc0c0ce8676e568298f00b2d49180138809a2'

    return token


def get_qubo(G, lagrange, n):
    """Returns a dictionary representing a QUBO"""

    #Number of nodes
    N = n

    # Empty dict - QUBO
    Q = defaultdict(float)

    # Constraint for visiting each node just once and using an edge once
    for edge in G: #iterate through each edge
        for stop_1 in range(n): #iterate through each possible departing stop
            Q[((edge, stop_1), (edge, stop_1))] -= lagrange #algebraic FOIL
            for stop_2 in range(stop_1+1, n): #iterate through each possible arrival stop
                Q[((edge, stop_1), (edge, stop_2))] += 2.0*lagrange #algebraic FOIL

    # Constraint for visiting once city at a stop
    for stop in range(n): #iterate through each stop
        for node_1 in G: #iterate through each possible departing node
            Q[((node_1, stop), (node_1, stop))] -= lagrange #algebraic FOIL
            for node_2 in set(G)-{node_1}: #iterate through each possible arrival node
                Q[((node_1, stop), (node_2, stop))] += 2.0*lagrange #algebraic FOIL

    # Objective that minimizes distance it takes to visit each node
    for node_1, node_2 in itertools.combinations(G.nodes, 2): #combination of all edges
        for stop in range(n): #iterate through each stop
            arrival_stop = (stop + 1) % n #loop back to first stop

            # add distance to Qubo when node_1 is the departure node and node_2 is the arrival node
            Q[((node_1, stop), (node_2, arrival_stop))] += G[node_1][node_2]['weight']

            # add distance to Qubo when node_2 is the departure node and node_1 is the arrival node
            Q[((node_2, stop), (node_1, arrival_stop))] += G[node_1][node_2]['weight']

    offset = 2 * n * lagrange

    return Q, offset


def get_sampler(token):
    """Returns a sampler"""

    #use the hybrid_binary_quadratic_model_version2 sampler to solve qubo
    sampler = LeapHybridSampler(endpoint="https://cloud.dwavesys.com/sapi/", token=token, solver={'name': 'hybrid_binary_quadratic_model_version2'})

    return sampler


if __name__ == "__main__":

    lagrange = 4000
    n = 10
    G = nx.Graph()

    #Graph nodes with edge weights
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

    """
    G.add_weighted_edges_from([
        (0, 1, 2230),
        (0, 2, 1631),
        (0, 3, 1566),
        (0, 4, 1346),
        (0, 5, 1352),
        (0, 6, 1204),
        (0, 7, 1346),
        (0, 8, 1786),
        (1, 2, 845),
        (1, 3, 707),
        (1, 4, 1001),
        (1, 5, 947),
        (1, 6, 1484),
        (1, 7, 302),
        (1, 8, 266),
        (2, 3, 627),
        (2, 4, 773),
        (2, 5, 424),
        (2, 6, 644),
        (2, 7, 233),
        (2, 8, 1403),
        (3, 4, 302),
        (3, 5, 341),
        (3, 6, 1027),
        (3, 7, 876),
        (3, 8, 1200),
        (4, 5, 368),
        (4, 6, 916),
        (4, 7, 656),
        (4, 8, 388),
        (5, 6, 702),
        (5, 7, 344),
        (5, 8, 787),
        (6, 7, 563),
        (6, 8, 1034),
        (7, 8, 876),
    ])

    G.add_weighted_edges_from([
        (0, 1, 2230),
        (0, 2, 1631),
        (0, 3, 1566),
        (0, 4, 1346),
        (0, 5, 1352),
        (0, 6, 1204),
        (1, 2, 845),
        (1, 3, 707),
        (1, 4, 1001),
        (1, 5, 947),
        (1, 6, 1484),
        (2, 3, 627),
        (2, 4, 773),
        (2, 5, 424),
        (2, 6, 644),
        (3, 4, 302),
        (3, 5, 341),
        (3, 6, 1027),
        (4, 5, 368),
        (4, 6, 916),
        (5, 6, 702)
    ])


    G.add_weighted_edges_from([
        (0, 1, 3),
        (0, 2, 7),
        (0, 3, 6),
        (1, 2, 2),
        (1, 3, 4),
        (2, 3, 8)
    ])
    """

    Q, offset = get_qubo(G, lagrange, n)
    token = get_token()
    sampler = get_sampler(token)
    bqm = dimod.BinaryQuadraticModel.from_qubo(Q, offset=offset)

    start = timeit.default_timer()

    response = sampler.sample(bqm)

    stop = timeit.default_timer()

    print('Time: ', stop - start) #print runtime/response time of solver

    start = None
    sample = response.first.sample
    cost = response.first.energy
    route = [None] * n

    for (city, time), val in sample.items():
        if val:
            route[time] = city

    if start is not None and route[0] != start:
        # rotate to put the start in front
        idx = route.index(start)
        route = route[-idx:] + route[:-idx]

    if None not in route:
        print(route)
        print(cost)
