import utility

def main():
    a_ring = {}
    n = 5

    for i in range(n):
        utility.make_link(a_ring, i, (i + 1) % n)

    
    print(f'Nodes: {utility.len_node(a_ring)}')
    print(f'Edges: {utility.len_edges(a_ring)}')

    import pprint
    pprint.pprint(a_ring)
    
if __name__ == '__main__':
    main()