##import random
##guess = ''
##while guess not in ('heads', 'tails'):
##    print('Guess the coin toss! Enter heads or tails:')
##    guess = input()
##toss = random.randint(0, 1) # 0 is tails, 1 is heads
##if toss == guess:
##    print('You got it!')
##else:
##    print('Nope! Guess again!')
##    guesss = input()
##    if toss == guess:
##       print('You got it!')
##    else:
##        print('Nope. You are really bad at this game.')import random
##
##heads = 0
##for i in range(1, 1001):
##    if random.randint(0, 1) == 1:
##        heads = heads + 1
##    if i == 500:
##        print('Halfway done!')
##
##print('Heads came up ' + str(heads) + ' times.')

import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
    if toss == guess:
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
