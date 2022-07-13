from piece_options import PieceOptions as po

class GameSettings:
    def __init__(self, num_plrs: int, p1_color=po.blk, p2_color=po.red) -> None:
        self.num_plrs = num_plrs
        self.p1_color = p1_color
        self.p2_color = p2_color
    
    def get_num_players(self) -> int:
        return self.num_plrs
    
    def get_p1_color(self) -> str:
        return self.p1_color
    
    def get_p2_color(self) -> str:
        return self.p2_color