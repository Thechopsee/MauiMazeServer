class Edge:
    ID: int  
    MazeID: int
    Cell1: int
    Cell2: int
    def __init__(self, MazeID: int, Cell1: int, Cell2: int):
        self.ID: int = None  
        self.MazeID: int = MazeID
        self.Cell1: int = Cell1
        self.Cell2: int = Cell2
