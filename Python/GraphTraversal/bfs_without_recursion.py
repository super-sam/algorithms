from collections import deque


def make_link(graph, node1, node2) -> None:
    if node1 not in graph:
        graph[node1] = {}
    if node2 not in graph:
        graph[node2] = {}
    graph[node1][node2] = True
    graph[node2][node1] = True


def bfs_without_recursion(graph, vertex):
    visited = set()
    todo = deque()
    todo.append(vertex)
    visited.add(vertex)
    while todo:
        vertex = todo.popleft()
        for item in graph[vertex]:
            if item not in visited:
                visited.add(item)
                todo.append(item)
        print(vertex)


if __name__ == "__main__":
    import sys
    graph = {}
    for line in sys.stdin:
        p, q = line.split()
        make_link(graph, p, q)

    bfs_without_recursion(graph, tuple(graph.keys())[0])