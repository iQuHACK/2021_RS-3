# Covid-19 Vaccine Distribution Optimization

Franck N. Belemkoabga, Ritik Patnaik, Shayda Moezzi, Sebastian Monsalvo, Sophie Zhang

# Abstract

# Motivation and Goals
One of the biggest supply chain optimization problems of our generation is vaccine distribution, which is now more prevalent than ever before. Since the death toll due to the COVID-19 virus is increasing rapidly, it is imperative to distribute vaccines optimally and in an orderly fashion. Given a list of cities and the distances between each pair of cities, the goal is to find the shortest possible route that visits each city exactly once and returns to the distribution center.  The Travelling Salesman Problem (TSP) is a common optimization problem that can help find the shortest possible route. In addition, there are many other constraints to take into account such as how many vaccines can be shipped at a time, what temperature do the vaccines have to be stored at, and the expiration time of the vaccine.

The computational intensity of the TSP grows exponentially as more cities are added to the list. Using classical computers, solving this problem will eventually become infeasible. Quantum annealing technology, however, has the potential to solve this problem at an increased scale, as the bias and coupling constraints on the qubits creates an energy landscape and enables a much faster determination of the solution. Due to superposition of information, quantum annealing technology can consider a wide array of possible routes simultaneously, thereby making data processing more efficient.

# Description

# Future Work
So far our model works for finding the fastest route between a given set of cities with the given constraints above. Currently, someone has to manually input the coordinates and cost of passing through the edges in order to get an output. Our hope is that in the future the edge cost corresponding to the edges of a given city can be set to be a variable dependent on the risk factor of that city. This way, one would only have to input the risk factor of all the cities instead of having to calculate and input the edge cost of all the edges–which grow exponentially with respect to the number of cities in the network.


Method 1: choose highest risk factor nodes/cities, then optimize route using TSP\
Method 2: Knapsack (weight = max distance, value = number of vaccines needed/risk factor), then TSP\
Method 3: determine clusters of cities, choose which cluster based on average risk factor, then use TSP to travel within cluster\
Method 4: purely TSP\
