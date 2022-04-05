# Minimum Spanning Tree

### Cut
A cut in a graph is a partition of its vertices into two (nonempty) sets.. Example set of Gray vertices and White Vertices.

### Crossing Edge
A crossing edge connectes a vertex in one set with a vertex in the other set.

### Cut Property
Given any cut, the crossing edge of min weight is the MST.

<hr>

## Greedy Algorithm
- Start with all the edges colored grey.
- Find the cut with no black crossing edge; color it's min weight edge back.
- Repeat unit V - 1 edges are colored black

## Kruskal's Algorithm
- Traverse throught the edges in increasing order of weight
- Check if the new edge makes cycle
    - Yes, reject the edge
    - No, accepts the edge
- Stop if Vertex - 1 edges are connect 

## Prims's Algorithm
