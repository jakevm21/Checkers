from enum import Enum


class PieceOptions(Enum):
    red = "R"
    blk = "B"
    empty = 0
    red_reg = 1
    red_kng = 2
    blk_reg = 3
    blk_kng = 4
