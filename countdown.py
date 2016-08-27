#! /usr/bin/python3
# countdown.py - A simple countdown script.

import time, subprocess

timeLeft = 10
while timeLeft > 0:
    print(timeLeft)
    time.sleep(1)
    timeLeft = timeLeft - 1

# At the end of the countdown, play a sound file
subprocess.Popen(['see', 'alarm.wav'])
