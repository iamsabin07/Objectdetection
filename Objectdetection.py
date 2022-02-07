import cv2
import numpy as np
import pyautogui as pg

# to screenshot the screen
screenshot = pg.screenshot()

# to convert screenshot into BGR using numpy array
screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

# to locate the chess board in the screen
board = pg.locateOnScreen('board.png')

# to create a yellow border around the chess board
cv2.rectangle(screenshot,
              (board.left, board.top),
              (board.left + board.width, board.top + board.height),
              (0, 255, 255), 5)

# to show the screenshot with yellow border
cv2.imshow('Screenshot', screenshot)
cv2.waitKey(0)
cv2.destroyAllWindows()

