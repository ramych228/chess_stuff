import cv2
import numpy as np

from Clicker import Clicker
from ImagePreProcessing import ImagePreProcessing
from ImageProcessing import ImageProcessing
from Rectangular import Rectangular
import pyautogui

preprocessed_image = ImagePreProcessing(cv2.imread("lichess_screenshot.png", cv2.IMREAD_GRAYSCALE))
preprocessed_image.preprocess()

image = ImageProcessing(cv2.imread("lichess_screenshot2.png", cv2.IMREAD_GRAYSCALE), preprocessed_image.get_pieces(), preprocessed_image.get_board())

image.print_desk()

clicker = Clicker(preprocessed_image.get_board())
while(True):
    screenshot = pyautogui.screenshot()
    
    a = input()
    pyautogui.sleep(1)
    clicker.make_human_click(a)
