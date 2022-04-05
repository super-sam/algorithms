from dataclasses import dataclass
from typing import Final


@dataclass
class DiEdge:
    v: Final
    w: Final
    weight: Final

    @property
    def from_edge(self) -> int:
        return self.v
    
    @property
    def to_edge(self) -> int:
        return self.w
    
    @property
    def weight(self) -> float:
        return self.weight
