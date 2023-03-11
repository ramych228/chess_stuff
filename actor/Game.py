import pytesseract
import pyautogui
import cv2

from ChessBoard import ChessBoard
from ImageProcessing import ImageProcessing
from brain.chooser import Chooser
from brain.estimator import NaiveEstimator

class Game:
    def __init__(self, preprocessed_image):
        self.preprocessed_image = preprocessed_image

    def play(self):
        ai = NaiveEstimator()
        while(True):
            image = cv2.imread(pyautogui.screenshot(), cv2.IMREAD_GRAYSCALE)
            processed_image = ImageProcessing(cv2.imread("lichess_screenshot2.png", cv2.IMREAD_GRAYSCALE),
                                    self.preprocessed_image.get_pieces(), self.preprocessed_image.get_board())
            chess_board = ChessBoard(processed_image.get_desk())
            x_from, y_from, x_to, y_to = ai.get_move(chess_board)
