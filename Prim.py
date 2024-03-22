#import csv to read file with graph data
import csv

#this is a function to add vertices to the graph
def add_vertex(v):
  global graph
  if v not in graph:
    graph[v] = []
# each vertex has more edges added as they occur in the graph
def add_edge(vertex_1, vertex_2, edge_weight):
  global graph
  graph[vertex_1].append([vertex_2, edge_weight])
  graph[vertex_2].append([vertex_1, edge_weight])

"""
This is an optional implementation to view the graph
"""
def print_graph():
  global graph
  for vertex in graph:
    for edges in graph[vertex]:
      print(vertex, " -> ", edges[0], " edge weight: ", edges[1])
vertices =set()
graph ={}

#reading data
with open('doctorwho.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    next(csvFile)
    for lines in csvFile:
        if lines[0] not in graph:
                add_vertex(lines[0])
                vertices.add(lines[0])
        if lines[1] not in graph:
                add_vertex(lines[1])
                vertices.add(lines[1])
        add_edge(lines[0],lines[1],int(lines[2]))


def prims_algorithm(graph):
  minimum_spanning_tree =[]
  visited_vertices = set()
  global vertices
  initial_vertex =next(iter(vertices))
  print("Starting from \n",initial_vertex)
  visited_vertices.add(initial_vertex)
  while len(visited_vertices)<len(vertices):
    min_edge = None
    min_weight = float('inf')
    for vertex in visited_vertices:
      for edge in graph[vertex]:
          if edge[0] not in visited_vertices and edge[1]<min_weight:
            min_edge = (vertex,edge[0])
            min_weight = edge[1]
      
    if min_edge:
      minimum_spanning_tree.append((min_edge[0],min_edge[1],min_weight))
      visited_vertices.add(min_edge[1])
    else:
      initial_vertex =next(iter(vertices-visited_vertices))
      print()
      print("Finish at \n",initial_vertex)
      visited_vertices.add(initial_vertex)
  return minimum_spanning_tree


results = prims_algorithm(graph)
print(results)
print(len(graph))
print(len(results))
