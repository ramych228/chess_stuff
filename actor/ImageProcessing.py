import os
import cv2
import numpy as np
from Rectangular import Rectangular


class ImageProcessing:
    def __init__(self, image, pieces, board):
        self.image = image
        self.pieces = pieces
        self.board = board
        self.len = self.board.get_height() // 8

    def get_figure_name(self, i, j):
        cnt_pixels_black = 0
        cnt_pixels_white = 0
        for row in range(self.len):
            for col in range(self.len):
                if self.image[row + self.board.get_left_up()[1] + i * self.len][
                    col + self.board.get_left_up()[0] + j * self.len] == 0:
                    cnt_pixels_black += 1
                if self.image[row + self.board.get_left_up()[1] + i * self.len][
                    col + self.board.get_left_up()[0] + j * self.len] == 255:
                    cnt_pixels_white += 1

        for piece in self.pieces:
            if abs(piece[1] - cnt_pixels_black / (self.len * self.len) * 100) < 0.1:
                return piece[0]
            if abs(piece[1] - cnt_pixels_white / (self.len * self.len) * 100) < 0.1:
                return piece[0]
        return "empty"

    def get_beautiful_symbol_of_piece(self, piece):
        if piece == "black_rook":
            return "♜"
        elif piece == "black_knight":
            return "♞"
        elif piece == "black_elephant":
            return "♝"
        elif piece == "black_queen":
            return "♛"
        elif piece == "black_king":
            return "♚"
        elif piece == "black_pawn":
            return "♟"
        elif piece == "white_king":
            return "♔"
        elif piece == "white_elephant":
            return "♗"
        elif piece == "white_knight":
            return "♘"
        elif piece == "white_rook":
            return "♖"
        elif piece == "white_pawn":
            return "♙"
        elif piece == "white_queen":
            return "♕"
        elif piece == "e":
            return ' '

    def print_desk(self):
        for i in range(8):
            for j in range(8):
                print(self.get_beautiful_symbol_of_piece(self.get_figure_name(i, j)[:-4]), end='\t')
            print()

    def get_desk(self):
        ar = np.eye(8, 8)
        for i in range(8):
            for j in range(8):
                ar[i][j] = self.get_figure_name(i, j)[:-4]
        return ar
