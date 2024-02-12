class Edge:
    Cell1: int
    Cell2: int
    def __init__(self, Cell1: int, Cell2: int):
        self.Cell1: int = Cell1
        self.Cell2: int = Cell2

    def serialize(self):
        return {
            'Cell1': self.Cell1,
            'Cell2': self.Cell2,
        }
