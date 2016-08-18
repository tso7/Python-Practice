def ListEnglish(inputList):
    for i in range(0, len(inputList)-1):
        print(str(inputList[i]) + ', ' , end='')
    print ('and ' + str(inputList[i+1]))

spam = ['apples', 'bananas', 'tofu', 'cats', 1, 4.5, -42]
ListEnglish(spam)
