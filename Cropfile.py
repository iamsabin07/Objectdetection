import cv2
import pyautogui as pg
import numpy as np

# to screenshot the screen
screenshot = pg.screenshot()

# to convert screenshot into BGR using numpy array
screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

# to locate the chess board in the screen
board = pg.locateOnScreen('board.png')

# x= x coordinate of board
x = board.left

# x= y coordinate of board
y = board.top

# x= width of board
w = board.width

# x= height of board
h = board.height

# to crop the chess board in the screenshot using slice feature of numpy array
crop_image = screenshot[y:y+h, x:x+w]

# to show the cropped image
cv2.imshow('Cropped Image', crop_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
