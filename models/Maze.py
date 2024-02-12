import datetime
from models.Edge import Edge
class Maze:
    ID: int
    UserID :int 
    Type :str
    CreationDate :datetime
    StartCell  :int
    EndCell:int
    Size :int
    Edges =[]
    def __init__(self, UserID, Type, CreationDate,StartCell,EndCell,Size):
        self.ID = None  
        self.UserID = UserID
        self.Type = Type
        self.CreationDate = CreationDate
        self.StartCell=StartCell
        self.EndCell=EndCell
        self.Size=Size
