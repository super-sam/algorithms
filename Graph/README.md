## Kruskal Algorithim
**Used to find Minimum Spanning Tree of he whole graph. Can be used for disjoint graph**
Total Edges in MST is Total Vertex - 1

- Use Heap to add all egdes 
- While all the edge isnt found
- Take a edge, check it there will be a cycle or not
- If cycle(union find), 
    ignore the edge
  Else
    Add the Edge


## Prim Algorithm
** Used to find mst from a Vertex**
- Use Heap to add all egdes from the selected vertex
- For each edge with min weight, visit the from and to vertex if not visited,
- Visit the vertex by adding all the edges to the heap 

