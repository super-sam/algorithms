# Union Find
This algo helps in finding if there exist any path from 1 point to another point.

## Is Connected to relation
- Reflexive: _p_ is connected to _p_.
- Symmetric: if _p_ is connected to _q_, then _q_ is connected to _p_.
- Transitive: if _p_ is connected to _q_ and _q_ is connected to _r_ then _p_ is connected to _r_.

## Quick Find
Initialise all with unique key

if p is connected with q then 
all item with key as q's key 
is p's key

## Quick Union
Initialise all with unique key

union p, q
make p's root to q'root

connected p, q
if p's root and q's root is same then connected

## Weighted Quick Union
Put smaller tree below the larger tree in union


## Weighted Quick Union with Path compression
While finding root make child's root to point it's grand parent

## Percolation
If there exist a path from top to bottom
  