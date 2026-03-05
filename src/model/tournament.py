from dataclasses import dataclass, field

@dataclass
class tournament:
    tournID: int
    tournName: str
    hostID: int
    hostName: str
    creation_date: tuple[int, int, int]
    players: list = field(default_factory=list)
    
    def addPlayers(self, newPlayers):
         for new in newPlayers:
            self.players.append(new)
            
    def setTournName(self, name):
        self.tournName = name

    def setTournID(self, id):
        self.tournID = id

    def setHostID(self, id):
        self.hostID = id
    
    def setHostName(self, name):
        self.hostName = name

    def setCreationDate(self, month, day, year):
        self.creation_date = (month, day, year)

    