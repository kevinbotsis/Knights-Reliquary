from dataclasses import dataclass

@dataclass
class tournament:
    tournID: int
    tournName: str
    hostID: int
    hostName: str
    creation_date: tuple[int, int, int]