def make_link(g, node1, node2):
    if node1 not in g:
        g[node1] = {}
    g[node1][node2] = 1

    if node2 not in g:
        g[node2] = {}
    g[node2][node1] = 1

def len_node(g):
    return len(g)

def len_edges(g):
    return sum([len(g[key]) for key in g.keys()]) // 2