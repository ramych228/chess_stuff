import os
import cv2
import numpy as np
from Rectangular import Rectangular

class ImagePreProcessing:
    def __init__(self, image):
        self.image = image
        self.height = image.shape[0]
        self.width = image.shape[1]
        self.pieces = []
        self.board = None

    def get_board(self):
        return self.board

    def get_pieces(self):
        return self.pieces
    def save(self, file_name):
        cv2.imwrite(file_name, self.image)

    def get_colors_intensity(self):
        colors_intensity = [0] * 256
        for row in range(self.height):
            for col in range(self.width):
                colors_intensity[int(self.image[row][col])] += 1
        return colors_intensity

    def get_sorted_colors_intensity(self):
        sorted_colors_intensity = []
        colors_intensity = self.get_colors_intensity()
        for i in range(256):
            sorted_colors_intensity.append((colors_intensity[i], i))

        sorted_colors_intensity.sort(key=lambda color: color[0], reverse=True)
        return sorted_colors_intensity

    def get_black_and_white_cells_color(self):
        sorted_colors_intensity = self.get_sorted_colors_intensity()
        return sorted_colors_intensity[3][1], sorted_colors_intensity[2][1]

    def check_pixels_around(self, row, col, color):
        is_this_color = True
        for i in range(6):  # 5 - also works, but for the best accuracy u can take up to 10 (more is too long)
            for j in range(2): # u can play with this constants
                if ~(row + i < self.height and col + j < self.width and self.image[row + i][col + j] == color):
                    is_this_color = False
        return is_this_color

    def get_left_up_corner_coordinates(self):
        black, white = self.get_black_and_white_cells_color()
        x, y = 0, 0
        finish_flag = False
        for row in range(self.height//10, self.height):
            if finish_flag:
                break
            for col in range(self.width):
                if self.check_pixels_around(row, col, black) or self.check_pixels_around(row, col, white):
                    y, x = row, col
                    finish_flag = True
                    break
        return x, y

    def get_board_coordinates(self):
        black, white = self.get_black_and_white_cells_color()
        left_up_x, left_up_y = self.get_left_up_corner_coordinates()
        x = left_up_x
        y = left_up_y
        while self.image[left_up_y][x] == black or self.image[left_up_y][x] == white:
            x += 1
        right_up_x = x - 1
        right_up_y = left_up_y

        while self.image[y][left_up_x] == black or self.image[y][left_up_x] == white:
            y += 1
        left_down_x = left_up_x
        left_down_y = y - 1

        right_down_x, right_down_y = right_up_x, left_down_y

        self.board = Rectangular(left_up_x, left_up_y, right_up_x, right_up_y, left_down_x, left_down_y, right_down_x,
                                 right_down_y)
        return self.board

    def get_figure_images(self):
        len = self.board.get_height() // 8
        for i in range(8):
            for j in range(8):
                row = i * len
                col = j * len
                a = np.eye(len, len)
                for r in range(row, row+len):
                    for c in range(col, col + len):
                        a[r-row][c-col] = self.image[self.board.get_left_up()[1] + r][self.board.get_left_up()[0] + c]
                cv2.imwrite("cells\\" + str(i) + "," + str(j) + ".png", a)
                if i == 0:
                    if j == 0:
                        cv2.imwrite("chess_pieces\\white_rook.png", a)
                    elif j == 1:
                        cv2.imwrite("chess_pieces\\white_knight.png", a)
                    elif j == 2:
                        cv2.imwrite("chess_pieces\\white_elephant.png", a)
                    elif j == 3:
                        cv2.imwrite("chess_pieces\\white_king.png", a)
                    elif j == 4:
                        cv2.imwrite("chess_pieces\\white_queen.png", a)
                elif i == 1 and j == 0:
                    cv2.imwrite("chess_pieces\\white_pawn.png", a)
                elif i == 6 and j == 0:
                    cv2.imwrite("chess_pieces\\black_pawn.png", a)
                elif i == 7:
                    if j == 0:
                        cv2.imwrite("chess_pieces\\black_rook.png", a)
                    elif j == 1:
                        cv2.imwrite("chess_pieces\\black_knight.png", a)
                    elif j == 2:
                        cv2.imwrite("chess_pieces\\black_elephant.png", a)
                    elif j == 3:
                        cv2.imwrite("chess_pieces\\black_king.png", a)
                    elif j == 4:
                        cv2.imwrite("chess_pieces\\black_queen.png", a)

    def get_percentage_of_each_piece(self):
        for filename in os.listdir("chess_pieces"):
            cur_img = cv2.imread("chess_pieces\\" + filename, cv2.IMREAD_GRAYSCALE)
            cnt_pixels = 0
            for row in range(cur_img.shape[0]):
                for col in range(cur_img.shape[1]):
                    if (filename[0] == 'b' and cur_img[row][col] == 0) or (filename[0] == 'w' and cur_img[row][col] == 255):
                        cnt_pixels += 1
            self.pieces.append((filename, cnt_pixels / (cur_img.shape[0] * cur_img.shape[1]) * 100))

    def print_percentage(self):
        self.get_percentage_of_each_piece()
        for piece in self.pieces:
            print(piece[0], " : ", piece[1])

    def get_figure_name(self, i, j):
        cnt_pixels_black = 0
        cnt_pixels_white = 0
        for row in range(self.board.get_height() // 8):
            for col in range(self.board.get_height() // 8):
                if self.image[row + self.board.get_left_up()[1] + i * self.board.get_height() // 8][col + self.board.get_left_up()[0] + j * self.board.get_height() // 8] == 0:
                    cnt_pixels_black += 1
                if self.image[row + self.board.get_left_up()[1] + i * self.board.get_height() // 8][col + self.board.get_left_up()[0] + j * self.board.get_height() // 8] == 255:
                    cnt_pixels_white += 1

        for piece in self.pieces:
            if abs(piece[1] - cnt_pixels_black / (self.board.get_height() // 8 * self.board.get_height() // 8) * 100) < 0.1:
                return piece[0]
            if abs(piece[1] - cnt_pixels_white / (self.board.get_height() // 8 * self.board.get_height() // 8) * 100) < 0.1:
                return piece[0]
        return "empty"

    def preprocess(self):
        self.get_board_coordinates()
        self.get_figure_images()
        self.get_percentage_of_each_piece()
