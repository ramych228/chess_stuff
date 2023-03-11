from Rectangular import Rectangular
import pyautogui
import random


class Clicker:
    def __init__(self, board):
        self.board = board
        self.cell_len = self.board.get_height() // 8

    def make_move(self, a, b):  # a = (y, x) = (row, col)
        pyautogui.sleep(0.1)
        pyautogui.click(self.get_coord(a)[0], self.get_coord(a)[1])
        pyautogui.sleep(random.uniform(0.3, 1.1))
        pyautogui.click(self.get_coord(b)[0], self.get_coord(b)[1])

    def make_human_move(self, a, b):
        pyautogui.sleep(0.1)
        pyautogui.click(self.to_click(a))
        pyautogui.sleep(random.uniform(0.3, 1.1))
        pyautogui.click(self.to_click(b))

    def to_click(self, a):
        to_click = self.get_coord((int(a[1]) - 1, 7 - (ord(a[0]) - ord('a'))))
        return to_click[0], to_click[1]

    def make_click(self, a):
        pyautogui.sleep(0.1)
        pyautogui.click(self.get_coord(a)[0], self.get_coord(a)[1])

    def make_human_click(self, a):
        pyautogui.sleep(0.1)
        pyautogui.click(self.to_click(a))

    def get_coord(self, a):
        return self.board.get_left_up()[0] + self.cell_len * a[1] + self.cell_len // 2, \
               self.board.get_left_up()[1] + self.cell_len * a[0] + self.cell_len // 2
