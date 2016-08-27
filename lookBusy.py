#! /usr/bin/python3

import pyautogui, time, random

# Run until interrupted by keyboard
print('Looking good...')
try:
    while True:
        # Move mouse randomly every 10 seconds
        possibleMove = [(0,1),(1,0),(-1,0),(0,-1)]
        pyautogui.moveRel(possibleMove[random.randint(0,3)])
        time.sleep(10)
except KeyboardInterrupt:
    print('\nScript stopped.')
