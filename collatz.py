def collatz(num):
    if not num % 2:
        val = num // 2
    else:
        val = 3 * num + 1
    print(val)
    return val

print ('Enter number: ')
while True:
    try:
        result = input()
        int(result)
        break
    except ValueError:
        print('Invalid Number. Try again: ')

while result != 1:
   result = collatz(int(result))
print ('Program ended')
    
