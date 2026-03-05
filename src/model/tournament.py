from dataclasses import dataclass

@dataclass
class tournament:
    tournID: int
    tournName: str
    hostID: int
    hostName: str
    creation_date: tuple[int, int, int]
    players: []

    def addPlayers(newPlayers):
        for new in newPlayers:
            players.add[new]
            
    def setTournName(self, name):
        self.tournName = name

    def setTournID(self, id):
        self.tournID = id