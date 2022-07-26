from typing import List, Tuple
from piece_options import *


class Piece:
    def __init__(self, color: str, rank: int) -> None:
        self.color = color
        self.rank = rank

    def rank_up(self):
        self.rank = KNG

    def get_color(self):
        return self.color

    def get_rank(self):
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
    
    def get_moves(self, row: int, col: int) -> List[Tuple[int, int]]:
        moves = []

        if row < NUM_SQS - 1:
            if col > 0:
                moves.append((row + 1, col - 1))
            if col < NUM_SQS - 1:
                moves.append((row + 1, col + 1))
        if self.rank == KNG and row > 0:
            if col > 0:
                moves.append((row - 1, col - 1))
            if col < NUM_SQS - 1:
                moves.append((row - 1, col + 1))

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

    def get_moves(self, row: int, col: int) -> List[Tuple[int, int]]:
        moves = []

        if row > 0:
            if col > 0:
                moves.append((row - 1, col - 1))
            if col < NUM_SQS - 1:
                moves.append((row - 1, col + 1))
        if self.rank == KNG and row < NUM_SQS - 1:
            if col > 0:
                moves.append((row + 1, col - 1))
            if col < NUM_SQS - 1:
                moves.append((row + 1, col + 1))
        
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
