import datetime
from Edge import Edge
class Maze:
    ID: int
    UserID :int 
    Type :str
    CreationDate :datetime
    Edges =[]
    def __init__(self, UserID, Type, CreationDate):
        self.ID = None  
        self.UserID = UserID
        self.Type = Type
        self.CreationDate = CreationDate
