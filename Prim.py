import csv

def add_vertex(v):
  global graph
  if v not in graph:
    graph[v] = []

def add_edge(vertex_1, vertex_2, edge_weight):
  global graph
  graph[vertex_1].append([vertex_2, edge_weight])


def print_graph():
  global graph
  for vertex in graph:
    for edges in graph[vertex]:
      print(vertex, " -> ", edges[0], " edge weight: ", edges[1])
names =[]
graph ={}
with open('doctorwho.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    next(csvFile)
    for lines in csvFile:
        if lines[0] not in graph:
                add_vertex(lines[0])
                names.append(lines[0])
    file.seek(0)
    next(csvFile)
    count=0
    for lines in csvFile:
        add_edge(lines[0],lines[1],lines[2])
        count+=1
#print(count)
# print(graph)
# print(len(graph))
#print_graph()