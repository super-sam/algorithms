from __future__ import annotations
from functools import total_ordering
from dataclasses import dataclass, field


@dataclass
class Node:
    key: Any
    val: Any
    max: Any = field(default=None)
    count: int = field(default=1)
    left: Node = field(default=None, repr=False)
    right: Node = field(default=None, repr=False)


class IST:
    self