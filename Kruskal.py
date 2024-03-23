# Importing required library
import csv

# Function to initialize a new set for a vertex
def make_set(vert):
    return {vert}

# Function to find the set in which the given vertex belongs
def find_set(vert, sets):
    for s in sets:
        if vert in s:
            return s

# Function to merge two sets
def merge_sets(set1, set2, sets):
    sets.remove(set1)
    sets.remove(set2)
    merged_set = set1.union(set2)
    sets.append(merged_set)

# Function to add an edge to the minimum spanning tree
def add_edge(edge, minimum_spanning_tree, sets):
    vertex1, vertex2, weight = edge
    set1 = find_set(vertex1, sets)
    set2 = find_set(vertex2, sets)
    if set1 != set2:
        minimum_spanning_tree.append(edge)
        merge_sets(set1, set2, sets)

# Function to read graph data from CSV and initialize vertices and edges
def read_graph():
    vertices = set()
    edges = []
    with open('doctorwho.csv', mode='r') as file:
        csvFile = csv.reader(file)
        next(csvFile)
        for lines in csvFile:
            vertices.add(lines[0])
            vertices.add(lines[1])
            edges.append((lines[0], lines[1], int(lines[2])))
    return vertices, edges

# Kruskal's algorithm implementation
def kruskal_algorithm(vertices, edges):
    minimum_spanning_tree = []
    sets = [make_set(vert) for vert in vertices]
    sorted_edges = sorted(edges, key=lambda x: x[2])
    for edge in sorted_edges:
        add_edge(edge, minimum_spanning_tree, sets)
    return minimum_spanning_tree

vertices, edges = read_graph()
results = kruskal_algorithm(vertices, edges)
print(results)
print("Number of vertices:", len(vertices))
print("Number of edges in the minimum spanning tree:", len(results))
