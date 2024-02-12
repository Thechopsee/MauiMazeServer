class MoveRecord:
    def __init__(self, mr_id,percentage_x, percentage_y, hit_wall,delta,cell):
        self.mrID = mr_id
        self.percentagex = percentage_x
        self.percentagey = percentage_y
        self.hitWall = hit_wall
        self.deltaTinMilisec=int(delta)
        self.cell=cell

# Example usage:
# move_record = MoveRecord(mr_id=1, position_x=2, position_y=3, percentage_x=0.5, percentage_y=0.8, hit_wall=True)
