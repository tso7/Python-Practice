import random

def checkInput(num):
    try:
        int(num)
        return True
    except ValueError:
        print ('Invalid number')
        return False

secretNum = random.randint(1,20)
print ('I am thinking of a number between 1 and 20.\nTake a guess.')
typedNum = input()
count = 1
while int(typedNum != secretNum):
    count += 1
    if int(typedNum) < 1 or int(typedNum) > 20:
        print ('Stop messing with the program please.')
    elif int(typedNum) < secretNum:
        print ('Your guess is too low.')
    else:
        print ('Your guess is too high.')
    print('Take a guess.')
    try:
        typedNum = input()
    except TypeError:
        print('Invalid entry')
print ('Good job! You guessed my number in ' + str(count) + ' guesses!')
