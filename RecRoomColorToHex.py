#!/usr/bin/env python3

# RecRoomColorToHex.py - Created by RealMCoded, @stuartt on Rec Room.
# Released under the GNU GPLv3 License. https://github.com/RealMCoded/RecRoomKeyboard/blob/main/LICENSE
# Repo - https://github.com/RealMCoded/RecRoomKeyboard/

# Requirements:
# pynput
# pyautogui

import pyautogui
import time
from pynput.keyboard import Controller
import math
from collections import Counter

def get_most_common_color(region):
    screenshot = pyautogui.screenshot(region=region)
    pixels = list(screenshot.getdata())
    most_common_pixel = Counter(pixels).most_common(1)[0][0]
    return most_common_pixel  # returns (r, g, b)

def color_distance(c1, c2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(c1, c2)))

def is_similar_color(c1, c2, tolerance=45):
    return color_distance(c1, c2) <= tolerance

# Color definitions. Uses the Apple ][ color palette.
WHITE = (253, 253, 253)   # 0
YELLOW = (250, 242, 0)    # 1
ORANGE = (253, 99, 0)     # 2
RED = (219, 2, 2)         # 3
PINK = (238, 2, 132)      # 4
VIOLET = (69, 0, 164)     # 5
BLUE = (0, 0, 211)        # 6
CYAN = (0, 173, 231)      # 7
LIME = (26, 184, 12)      # 8
GREEN = (0, 99, 7)        # 9
BROWN = (86, 40, 0)       # A
LTBROWN = (144, 111, 53)  # B
LTGREY = (191, 191, 191)  # C
GREY = (128, 128, 128)    # D
DKGREY = (62, 62, 62)     # E
FAUXBK = (35, 35, 35)     # F
BLACK = (0, 0, 0)         # NOTHING

def main():
    last_color = None
    hex = ""
    region = (799, 1087, 323, 53)  # (x, y, width, height). this variable will be different for you. i use a 1920x1200 monitor btw
    keyboard = Controller()

    print("Ready to read color data!")

    while True:
        current_color = get_most_common_color(region)
        if current_color != last_color:
            last_color = current_color

            if is_similar_color(current_color, BLACK):
                print("nothing")
            elif is_similar_color(current_color, WHITE):
                print("got hex 0")
                hex += "0"
            elif is_similar_color(current_color, YELLOW):
                print("got hex 1")
                hex += "1"
            elif is_similar_color(current_color, ORANGE):
                print("got hex 2")
                hex += "2"
            elif is_similar_color(current_color, RED):
                print("got hex 3")
                hex += "3"
            elif is_similar_color(current_color, PINK):
                print("got hex 4")
                hex += "4"
            elif is_similar_color(current_color, VIOLET):
                print("got hex 5")
                hex += "5"
            elif is_similar_color(current_color, BLUE):
                print("got hex 6")
                hex += "6"
            elif is_similar_color(current_color, CYAN):
                print("got hex 7")
                hex += "7"
            elif is_similar_color(current_color, LIME):
                print("got hex 8")
                hex += "8"
            elif is_similar_color(current_color, GREEN):
                print("got hex 9")
                hex += "9"
            elif is_similar_color(current_color, BROWN):
                print("got hex A")
                hex += "A"
            elif is_similar_color(current_color, LTBROWN):
                print("got hex B")
                hex += "B"
            elif is_similar_color(current_color, LTGREY):
                print("got hex C")
                hex += "C"
            elif is_similar_color(current_color, GREY):
                print("got hex D")
                hex += "D"
            elif is_similar_color(current_color, DKGREY):
                print("got hex E")
                hex += "E"
            elif is_similar_color(current_color, FAUXBK):
                print("got hex F")
                hex += "F"
            
            if len(hex) == 2:
                key = chr(int(hex, 16))
                print(f"Hex data: {hex}\nPressing Key {key}")
                keyboard.press(key.lower())
                time.sleep(0.5)
                keyboard.release(key.lower())
                hex = ""
                print("Ready for next input\n")

if __name__ == "__main__":
    main()