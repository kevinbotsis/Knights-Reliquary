from dataclasses import dataclass, field

@dataclass
class tournament:
    tournID: int
    hostID: int
    hostName: str

    def setTournID(self, number):
        self.tournID = number

    def setHostID(self, number):
        self.hostID = number

    def setHostName(self, name):
        self.hostName = name