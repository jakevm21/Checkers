from typing import List, Tuple
from piece_options import *
UP = 'u'
DOWN = 'd'
LEFT = 'l'
RIGHT = 'r'


class Piece:
    def __init__(self, color: str, rank: int) -> None:
        self.color = color
        self.rank = rank

    def rank_up(self) -> None:
        self.rank = KNG

    def get_color(self) -> str:
        return self.color

    def get_rank(self) -> int:
        return self.rank

    def get_moves(self, row: int, col: int) -> List[Tuple[int, int]]:
        pass

    def get_moves(self, row: int, col: int) -> List[Tuple[int, int]]:
        pass

    def get_cap_moves(self, row: int, col: int) -> List[Tuple[int, int]]:
        pass

class BlackPiece(Piece):
    def __init__(self, rank=REG) -> None:
        super().__init__(BLK, rank)

    def _can_cap(self, row: int, col: int, vert_dir: str, h_dir: str, brd: List[List[Piece]]) -> bool:
        if brd[row][col].get_color() == self.color:
            return False
        if vert_dir == UP and row < len(brd) - 1:
            if h_dir == LEFT:
                return col > 0 and not brd[row + 1][col - 1]
            else:
                return col < len(brd) - 1 and not brd[row + 1][col + 1]
        elif vert_dir == DOWN and row > 0:
            if h_dir == LEFT:
                return col > 0 and not brd[row - 1][col - 1]
            else:
                return col < len(brd) - 1 and not brd[row - 1][col + 1]

    def get_moves(self, row: int, col: int, brd: List[List[Piece]]) -> List[Tuple[int, int]]:
        moves = []
        u = row + 1
        r = col + 1
        d = row - 1
        l = col - 1

        if row < len(brd) - 1:
            if col > 0:
                if not brd[u][l]:
                    moves.append((u, l))
                elif self._can_cap(u, l, UP, LEFT, brd):
                    moves.append((row + 2, col - 2))
            if col < len(brd) - 1:
                if not brd[u][r]:
                    moves.append((u, r))
                elif self._can_cap(u, r, UP, RIGHT, brd):
                    moves.append((row + 2, col + 2))

        if self.rank == KNG and row > 0:
            if col > 0:
                if not brd[d][l]:
                    moves.append((d, l))
                elif self._can_cap(d, l, DOWN, LEFT, brd):
                    moves.append((row - 2, col - 2))
            if col < len(brd) - 1:
                if not brd[d][r]:
                    moves.append((d, r))
                elif self._can_cap(d, r, DOWN, RIGHT, brd):
                    moves.append((row - 2, col + 2))

        return moves

    def get_cap_moves(self, row: int, col: int) -> List[Tuple[int, int]]:
        moves = []

        if row + 2 <= NUM_SQS - 1:
            if col - 2 >= 0:
                moves.append((row + 2, col - 2))
            if col + 2 <= NUM_SQS - 1:
                moves.append((row + 2, col + 2))
        if self.rank == KNG and row - 2 >= 0:
            if col - 2 >= 0:
                moves.append((row - 2, col - 2))
            if col + 2 <= NUM_SQS - 1:
                moves.append((row - 2, col + 2))

        return moves

class RedPiece(Piece):
    def __init__(self, rank=REG) -> None:
        super().__init__(RED, rank)

    def _can_cap(self, row: int, col: int, vert_dir: str, h_dir: str,brd: List[List[Piece]]):
        if brd[row][col].get_color() == self.color:
            return False
        if vert_dir == UP and row < len(brd) - 1:
            if h_dir == LEFT:
                return col > 0 and not brd[row + 1][col - 1]
            else:
                return col < len(brd) - 1 and not brd[row + 1][col + 1]
        elif vert_dir == DOWN and row > 0:
            if h_dir == LEFT:
                return col > 0 and not brd[row - 1][col - 1]
            else:
                return col < len(brd) - 1 and not brd[row - 1][col + 1]

    def get_moves(self, row: int, col: int, brd: List[List[Piece]]) -> List[Tuple[int, int]]:
        moves = []
        u = row + 1
        r = col + 1
        d = row - 1
        l = col - 1

        if row > 0:
            if col > 0:
                if not brd[d][l]:
                    moves.append((d, l))
                elif self._can_cap(d, l, DOWN, LEFT, brd):
                    moves.append((row - 2, col - 2))
            if col < len(brd) - 1:
                if not brd[d][col + 1]:
                    moves.append((d, r))
                elif self._can_cap(d, r, DOWN, RIGHT, brd):
                    moves.append((row - 2, col + 2))

        if self.rank == KNG and row < len(brd) - 1:
            if col > 0:
                if not brd[u][l]:
                    moves.append((u, l))
                elif self._can_cap(u, l, UP, LEFT, brd):
                    moves.append((row + 2, col - 2))
            if col < len(brd) - 1:
                if not brd[u][r]:
                    moves.append((u, r))
                elif self._can_cap(u, r, UP, RIGHT, brd):
                    moves.append((row + 2, col + 2))

        return moves

    def get_cap_moves(self, row: int, col: int) -> List[Tuple[int, int]]:
        moves = []

        if row - 2 <= NUM_SQS - 1:
            if col - 2 >= 0:
                moves.append((row - 2, col - 2))
            if col + 2 <= NUM_SQS - 1:
                moves.append((row - 2, col + 2))
        if self.rank == KNG and row + 2 <= NUM_SQS - 1:
            if col - 2 >= 0:
                moves.append((row + 2, col - 2))
            if col + 2 <= NUM_SQS - 1:
                moves.append((row - 2, col + 2))

        return moves
