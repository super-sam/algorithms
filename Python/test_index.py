from dataclasses import dataclass
from functools import total_ordering
import heapq


@dataclass
@total_ordering
class Edge:
    edge_from: int
    edge_to: int
    weight: float

    def __eq__(self, __o: object) -> bool:
        return self.weight == __o.weight
    
    def __lt__(self, __o: object) -> bool:
        return self.weight < __o.weight

if __name__ == "__main__":
    pq = []
    heapq.heappush(pq, Edge(0, 1, 10))
    heapq.heappush(pq, Edge(0, 2, 5))
    heapq.heappush(pq, Edge(0, 3, 2))
    print(pq)

    