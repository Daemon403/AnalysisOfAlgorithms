# AnalysisOfAlgorithms
This is a project of the implementation ot the Kuskal and Prim Algorithms to find MST using greed methods
# Kruskal and Prim Minimum Spanning Tree Algorithms

This repository contains Python implementations of the Kruskal and Prim algorithms for finding the minimum spanning tree (MST) of a weighted graph. The code also includes functionalities for analyzing the time and space complexities of these algorithms.

## Kruskal Algorithm

### Description
The Kruskal algorithm is used to find the minimum spanning tree in a connected, undirected graph. It starts by sorting the edges of the graph based on their weights and then adds edges to the MST in ascending order of weights, ensuring that no cycles are formed.

### Usage
To use the Kruskal algorithm implementation, simply run the `kruskal_algorithm` function with the input graph represented as a list of edges.

## Prim Algorithm

### Description
The Prim algorithm is another method for finding the minimum spanning tree of a graph. It starts from an arbitrary vertex and grows the MST by adding the lightest edge that connects a vertex in the MST to a vertex outside of it.

### Usage
To use the Prim algorithm implementation, run the `prims_algorithm` function with the input graph represented as an adjacency list.

## Time Complexity Analysis

The code includes functions for analyzing the time complexity of both algorithms. It measures the execution time for different input sizes and plots a graph showing the relationship between input size and running time.

## Space Complexity Analysis

Similarly, the code provides functions to analyze the space complexity of the algorithms. It measures the space usage for different input sizes and plots a graph illustrating the space requirements as the input size increases.

## Generating Graphs

Additionally, the repository includes a function for generating random weighted graphs in CSV format. This can be useful for testing the algorithms on different graph structures.

## Visualization

Finally, the code includes functions for visualizing graphs and their minimum spanning trees using the NetworkX library and Matplotlib.

For detailed usage instructions and examples, refer to the code comments and function documentation.

