import math
print('Prime number detector')
while 1:
    divisors = []
    number = int(input('What number do you want to test?\n'))
    for x in range(1, number+1):
        if number / x == math.floor(number / x):
            divisors.append(x)
    if divisors == [1, number]:
        print(f'The number {number} is a prime number!')
    elif divisors == [1]:
        print(f'The number {number} is a prime number!')
    else:
        print(f'The number {number} is a composite number! It is divisble by {divisors}')