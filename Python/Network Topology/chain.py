import utility

def main():
    a_chain = {}
    n = 5
    for i in range(n - 1):
        utility.make_link(a_chain, i, i+1)
    
    print(f'Nodes: {utility.len_node(a_chain)}')
    print(f'Edges: {utility.len_edges(a_chain)}')

    import pprint
    pprint.pprint(a_chain)

if __name__ == '__main__':
    main()