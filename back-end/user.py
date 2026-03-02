from dataclasses import dataclass

@dataclass
class User:
    id: int
    displayName: str
    username: str
    password: str
    creation_date: tuple[int, int, int]
    host: bool

    #sets the users creation date to the current month/day/year
    def setCreationDate(self, month, day, year):
        self.creation_date = (month, day, year)
    
    def setID(self, number):
        self.id = number

    def setName(self, name):
        self.displayName = name

    def setUsername(self, profile):
        self.username = profile

    def setPassword(self, currentPass):
        self.password = currentPass
        
    def setHost(self, hosting):
        self.host = hosting

    def validateName(self):
        if (len(self.displayName) < 1 or len(self.displayName) > 100):
            return False
        else:
            return True

    def validateID(self):
        if (self.id < 1 or self.id is None):
            return False
        else:
            return True
        
    def checkHost(self):
        return self.host
    

def main():
    name = input("Please Enter Your Name: ")
    

main()