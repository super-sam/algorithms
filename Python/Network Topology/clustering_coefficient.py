import utility

def clustering_coefficient(graph, node):
    '''
    v: a node
    Kv: degree
    Nv: Number of links between neighbours of v

    cv(v) = (2 * Nv) / Kv(Kv - 1)

    '''
    neighbours = graph[node].keys()
    if len(neighbours) == 1: return 0.0

    links = 0

    for n1 in neighbours:
        for neighbour in neighbours:
            if neighbour in graph[n1]:
                links += 0.5
    return (2 * links) / (len(neighbours) * (len(neighbours) - 1))

if __name__ == '__main__':
    flights = [
        ("ORD", "SEA"), ("ORD", "LAX"), ('ORD', 'DFW'), ('ORD', 'PIT'),
        ('SEA', 'LAX'), ('LAX', 'DFW'), ('ATL', 'PIT'), ('ATL', 'RDU'),
        ('RDU', 'PHL'), ('PIT', 'PHL'), ('PHL', 'PVD'),
        ]
    
    graph = {}
    for (node1, node2) in flights:
        utility.make_link(graph, node1, node2)
    cvvs = []
    for node in graph.keys():
        cvvs.append(clustering_coefficient(graph, node))
    print(sum(cvvs) / len(graph))
        