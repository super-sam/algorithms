
def make_link(graph, node1, node2, weight):
    graph[node1][node2] = weight
    graph[node2][node1] = weight


if __name__ == "__main__":
    pass