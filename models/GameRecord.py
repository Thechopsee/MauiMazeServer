import json
class GameRecord:   
    def __init__(self, gr_id, maze_id, user_id, time_in_milliseconds, hit_walls_count, cell_path_string):
        self.grID = gr_id
        self.mazeID = maze_id
        self.userID = user_id
        self.timeInMilliSeconds = time_in_milliseconds
        self.hitWallsCount = hit_walls_count
        self.cellPathString = cell_path_string
        self.records=[]
        