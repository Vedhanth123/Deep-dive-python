from __future__ import annotations
from dataclasses import dataclass 

@dataclass
class Vector:

    x: float
    y: float

    def __truediv__(self, other: float) -> Vector:

        return Vector(self.x / other, self.y / other)

def main() -> None:

    point = Vector(1,2)
    print(point / 2) # this will usually throw an error because we can't use division operator on the Vector class
    

if __name__ == '__main__':

    main()