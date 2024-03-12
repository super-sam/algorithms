import heapq

from graph import Graph, Vertex, Edge

from typing import Dict

def dijkstra(dag, start_vertex: Vertex) -> Dict[str, int]:
    distances = {vertex: (float("inf"), None) for vertex in dag.graph}
    distances[start_vertex.name] = (0, None)
    minheap = [(0, start_vertex.name, None)]

    while minheap:
        current_distance, vertex_name, current_edge = heapq.heappop(minheap)
        current_vertex = dag.graph[vertex_name]
        if current_distance > distances[vertex_name][0]:
            continue
        distances[vertex_name] = (current_distance, current_edge)
        for edge in dag.edges(current_vertex):
            to_vertex = edge.to_vertex
            distance = current_distance + edge.weight
            heapq.heappush(minheap, (distance, to_vertex.name, edge))

    return distances

def path(distances, start_vertex, end_vertex):
    current_vertex = end_vertex
    result = []
    while current_vertex != start_vertex:
        result.append(current_vertex)
        _, from_edge = distances[current_vertex.name]
        current_vertex = from_edge.from_vertex

    result.append(start_vertex)
    return result[::-1]


if __name__ == "__main__":
    graph = Graph()
    a = Vertex("A")
    b = Vertex("B")
    c = Vertex("C")
    d = Vertex("D")
    e = Vertex("E")
    f = Vertex("F")
    graph.add_edge(a, b, 4)
    graph.add_edge(a, c, 2)
    graph.add_edge(b, d, 5)
    graph.add_edge(c, d, 3)
    graph.add_edge(c, e, 2)
    graph.add_edge(d, e, 1)
    graph.add_edge(d, f, 1)
    graph.add_edge(e, f, 4)
    print(dijkstra(graph, a)) # {'A': 0, 'B': 4, 'C': 2, 'D': 5, 'E': 5, 'F': 9}