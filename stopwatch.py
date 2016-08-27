#! /usr/bin/python3
# stopwatch.py - A simple stopwatch program.

import time, pyperclip

# Display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the \
stopwatch.\nPress Ctrl-C to quit.')
input()                    # press Enter to begin
print('Started.')
startTime = time.time()    # get the first lap's start time
lastTime = startTime
lapNum = 1

# Start tracking the lap times.
output = []
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        lapString = 'Lap #:'+ str(lapNum).rjust(3) +  str(totalTime).rjust(7)\
                                + '  ('+str(lapTime).rjust(6) +')'
        output.append(lapString)
        print(lapString, end='')
        lapNum += 1
        lastTime = time.time() # Reset the last lap time
except KeyboardInterrupt:
    # Handle keyboard interrupt to prevent program from stopping abruptly
    text = '\n'.join(output)
    pyperclip.copy(text)
    print('\nDone. The lap times have been copied to the clipboard.')
