from queue import Queue, LifoQueue
from collections import UserDict
import copy
import typing

# class Edge:
#     def __init__(self, vertex1, vertex2, directed=False):
#         self.vertex1 = vertex1
#         self.vertex2 = vertex2
#         self.directed = directed
#
#     def __eq__(self, other):
#         if isinstance(other, Edge):
#             if not {self.vertex1, self.vertex2}.difference({other.vertex1, other.vertex2}):
#                 return True
#         return False
#
#


class Vertex:

    def __init__(self, _id):
        self.id = _id
        self.explored = False
        self.distance = 0
        self.finish_time = None

    def __repr__(self):
        return str(self.id)


class Graph(UserDict):
    # def without_vertex(self, vertex):
    #     graph_copy = copy.deepcopy(self)
    #     for vertex2, edges in self.data.items():
    #         if vertex2 == vertex:
    #             graph_copy.pop(vertex2)
    #             continue
    #         for vertex_edge in edges:
    #             if vertex_edge == vertex:
    #                 graph_copy[vertex2].remove(vertex_edge)
    #     return graph_copy

    def __setitem__(self, key: Vertex, value):
        self.data[int(key.id)] = value

    def __getitem__(self, item: Vertex):
        if isinstance(item, int):
            return self.data[item]
        return self.data[int(item.id)]

    def reverse(self):
        new_graph = Graph()
        for vertex, edges in self.items():
            for edge_vertex in edges:
                if new_graph.get(edge_vertex):
                    new_graph[edge_vertex].append(vertex)
                else:
                    new_graph[edge_vertex] = [vertex]
        self.data = new_graph.data


def init_vertexes(dataset_path):
    graph = Graph()
    with open(dataset_path) as dataset:
        for n, row in enumerate(dataset.readlines()):
            print(n)
            vertex_id, edge = row.strip().split()
            vertex = Vertex(vertex_id)
            vertex2 = Vertex(edge)
            if graph.get(vertex):
                graph[vertex].append(vertex2)
            else:
                graph[vertex] = [vertex2]
    return graph


def breadth_first_search(graph: typing.Dict[Vertex, typing.List[Vertex]],
                         start_vertex: Vertex):
    queue = Queue()
    start_vertex.explored = True
    queue.put(start_vertex)
    while not queue.empty():
        vertex = queue.get()
        for vertex2 in graph[vertex]:
            if not vertex2.explored:
                vertex2.explored = True
                vertex2.distance = vertex.distance + 1
                queue.put(vertex2)


def check_connectivity(graph: typing.Dict[Vertex, typing.List[Vertex]]):
    for vertex in graph:
        if not vertex.explored:
            breadth_first_search(graph, vertex)

    return [v for v in Vertex.all_vertexes if not v.explored]


def depth_first_search(graph: typing.Dict[Vertex, typing.List[Vertex]],
                       start_vertex: Vertex, queue: LifoQueue = None):
    if not queue:
        queue = LifoQueue()
    start_vertex.explored = True
    queue.put(start_vertex)
    for vertex in graph[start_vertex]:
        if not vertex.explored:
            depth_first_search(graph, vertex, queue)


def topological_search():
    pass


def depth_first_search_(graph: typing.Dict[Vertex, typing.List[Vertex]],
                       start_vertex: Vertex, queue: LifoQueue = None):
    if not queue:
        queue = LifoQueue()
    start_vertex.explored = True
    queue.put(start_vertex)
    for vertex in graph[start_vertex]:
        if not vertex.explored:
            depth_first_search(graph, vertex, queue)


def dfs_loop(graph):
    vertexes_processed = 0
    for vertex in graph:
        depth_first_search(graph, vertex)


def kosaraju():
    pass
