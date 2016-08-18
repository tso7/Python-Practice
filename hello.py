#This program says Hello World and asks for my name

print('Hello world!')

print('What is your name?') # ask for their name
myName = input()

print('It\'s good to meet you ' + myName)
print('The length of your name is: ' + str(len(myName)))

print('What is your age?')
myAge = input() #ask for their age

print('You will be ' +str(int(myAge)+1) + ' in a year.')
