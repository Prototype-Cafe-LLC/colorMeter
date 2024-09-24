import os
import time
import pyautogui


def color_meter():
    """
    color_meter is a function that measures the color of where cursor is pointing
    it keeps running until the user presses the 'q' key or ctrl+c
    """

    while True:
        # take cursor position on entire screen
        x, y = pyautogui.position()
        # take screenshot
        screenshot = pyautogui.screenshot(region=(x, y, 1, 1))
        # get color of pixel at cursor position
        color = screenshot.getpixel((0, 0))
        # print color
        # print("rgb(", str(color[0]), ",", str(color[1]), ",", str(color[2]), ")")
        # print in #RRGGBB format
        print("#%02x%02x%02x" % (color[0], color[1], color[2]))


if __name__ == "__main__":
    color_meter()
