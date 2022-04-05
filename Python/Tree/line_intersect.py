"""
    Put all x-coordinates of in a heap along with Line (x, Line)
    Insert y-coordinates into a RBT
    Delete y-coordinates from RBT when line ends
    Range search for vertical lines in RBT

    Algo
    - Sweep in the plain from left to right accross x axis
    - On Left Point of Horizontal Line - Insert (y Point, Line) in RBT
    - On Right Point of Horizontal Line - Delete (y Point) of Line in RBT
    - On Left Point of Vertical Line - Make range search in RBT for y points in Line

"""

from __future__ import annotations
from collections import namedtuple
from dataclasses import dataclass
import heapq
from typing import List, Tuple, NamedTuple
from Tree import oned_range_search

Point: NamedTuple[int] = namedtuple('Point', ['x', 'y'])


@dataclass
class Line:
    left: Point
    right: Point

    @staticmethod
    def is_horizontal(line: Line) -> bool:
        return line.left.y == line.right.y and line.left.x < line.right.x

    @staticmethod
    def is_vertical(line: Line) -> bool:
        return line.left.x == line.right.x and line.left.y < line.right.y


def get_xpoints_heap(lines: List[Line]) -> List[Tuple[int, Line]]:
    points = []
    for line in lines:
        heapq.heappush(points, (line.left.x, line))
        if Line.is_horizontal(line):
            heapq.heappush(points, (line.right.x, line))

    return points


def get_intersection_points(point_heap: List[Tuple[int, Line]]) -> Tuple[Tuple[Line]]:
    intersecting_points: List[Tuple[Line, Tuple[Line]]] = []
    rbt: oned_range_search.BST = oned_range_search.BST()
    while point_heap:
        x, line = heapq.heappop(point_heap)
        if Line.is_vertical(line):
            if rbt.range_count(line.left.y, line.right.y):
                intersecting = rbt.range_search(line.left.y, line.right.y)
                print(f"{line} is intersecting with {intersecting}")
                intersecting_points.append((line, tuple(map(lambda n: n.val, intersecting))))
        elif x == line.right.x:
            node = rbt.select(line.left.y)
            rbt.del_node(node)
        else:
            rbt.put(line.left.y, line)
    return tuple(intersecting_points)


if __name__ == '__main__':
    import sys
    lines = []
    data = """10 10 100 10
            20 30 60 30
            25 40 45 40
            30 70 80 70
            50 20 50 60
            95 5 95 15
            110 60 110 150
            200 8 200 120
            105 105 120 105
            51 60 111 60"""
    # for line in sys.stdin:
    for line in data.split("\n"):
        x1, y1, x2, y2 = tuple(map(int, line.split()))
        lines.append(Line(Point(x1, y1), Point(x2, y2)))

    import pprint
    # pprint.pprint(lines)

    points = get_xpoints_heap(lines)
    # pprint.pprint(points)

    intersection_lines: Tuple[Tuple[Line]] = get_intersection_points(points)

    pprint.pprint(intersection_lines)

    # for line in [hl1, hl2]:
    #     heapq.heappush(points, (line.left.x, line))
    #     heapq.heappush(points, (line.right.x, line))
    #
    #
    # import pprint
    # pprint.pprint(points)