import numpy as np

from ChessPieces import ChessPieces


class ChessBoard:
    def __init__(self, ar):
        self.cells = np.eye(8, 8)
        for i in range(8):
            for j in range(8):
                if ar[i][j] == "e":
                    self.cells[i][j] = ChessPieces.empty
                elif ar[i][j] == "white_pawn":
                    self.cells[i][j] = ChessPieces.white_pawn
                elif ar[i][j] == "white_knight":
                    self.cells[i][j] = ChessPieces.white_knight
                elif ar[i][j] == "white_elephant":
                    self.cells[i][j] = ChessPieces.white_bishop
                elif ar[i][j] == "white_rook":
                    self.cells[i][j] = ChessPieces.white_rook
                elif ar[i][j] == "white_queen":
                    self.cells[i][j] = ChessPieces.white_queen
                elif ar[i][j] == "white_king":
                    self.cells[i][j] = ChessPieces.white_king
                elif ar[i][j] == "black_pawn":
                    self.cells[i][j] = ChessPieces.black_pawn
                elif ar[i][j] == "black_knight":
                    self.cells[i][j] = ChessPieces.black_knight
                elif ar[i][j] == "black_elephant":
                    self.cells[i][j] = ChessPieces.black_bishop
                elif ar[i][j] == "black_rook":
                    self.cells[i][j] = ChessPieces.black_rook
                elif ar[i][j] == "black_queen":
                    self.cells[i][j] = ChessPieces.black_queen
                elif ar[i][j] == "black_king":
                    self.cells[i][j] = ChessPieces.black_king

    def get_cell(self, i, j):
        return self.cells[i][j]

    def get_cells(self):
        return self.cells
