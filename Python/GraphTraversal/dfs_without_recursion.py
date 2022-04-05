def make_link(graph, node1, node2):
    if node1 not in graph:
        graph[node1] = {}
    if node2 not in graph:
        graph[node2] = {}

    graph[node1][node2] = 1
    graph[node2][node1] = 1


def dfs(graph, vertex):
    todo = []
    visited = set()
    todo.append(vertex)
    visited.add(vertex)
    while todo:
        vertex = todo.pop()
        neighbours = graph[vertex]
        for neigh in neighbours:
            if neigh not in visited:
                visited.add(neigh)
                todo.append(neigh)
        print(vertex)


if __name__ ==  "__main__":
    graph = {}
    import sys
    for line in sys.stdin:
        p, q = line.split()
        make_link(graph, p, q)

    dfs(graph, tuple(graph.keys())[0])
