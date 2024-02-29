## Shuffling
Traverse through all the items
for every index, create a random index between 0 and index. <br>
Interchange the items in the indexes.

## Selection Sort
Find the minimum at every iteration <br>
Replace the current with minumum

## Insertion Sort
For each iteration <br>
Make sure that the elements to the left are always in sorted order
 
 ## Shell Sort (h-sort)
 Extension of Inserstion Sort <br>
 The basic idea is to rearrange the elements so that, starting with a large gap, elements are compared that are increasingly closer together. <br>
 This allows smaller elements to "bubble" quickly towards the front of the list.
 

 ## Convex Hall
 ### How to find Counter Clock Wise rotation between 3 points
 2 x Area(a, b, c) = (bx - ax)(cy - ay) - (by - ay)(cx - ax)

 ## Merge Sort
 

# Sorting Properties
| Algo | Inplace | Stable | Worst | Average | Best | Remark|
|--|--|--|--|-- |--|--|
| Selection | Y| |N^2/2| N^2/2 | N^2/2 | N Exchanges|
| Insertion | Y | Y  | N^2| N^2/4 | N | Use for small N or Partially ordered items|
| Shell | Y | | ? | ? | N | Tight Code |
| Merge | | Y | NlgN | NlgN | NlgN | NlgN Guarenteed, Stable|
| Quick | Y | | N^2/2 | 2NlgN | NlgN | NlgN probabilistic Gurantee. Fastest. Must Shuffle |
| Quick 3 way | Y | | N^2/2 | 2NlgN | NlgN | NlgN probabilistic Gurantee. Fastest. Must Shuffle |
| Heap | Y | | NlgN | NlgN | NlgN | NlgN Guarented, Inplace|

