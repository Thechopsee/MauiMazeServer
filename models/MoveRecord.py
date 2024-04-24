class MoveRecord:
    def __init__(self, mr_id,percentage_x, percentage_y, hit_wall,delta,cell):
        self.mrID = mr_id
        self.percentagex = percentage_x
        self.percentagey = percentage_y
        self.hitWall = hit_wall
        self.deltaTinMilisec=int(delta)
        self.cell=cell