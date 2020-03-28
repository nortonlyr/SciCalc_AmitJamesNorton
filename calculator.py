import math
from random import randint

#### User Interface ####

def enter_num():
    num1 = float(input())
    return num1

#### Large Loop ####

def choose_op():
    print('1 Addition           2 Subtraction       3 Multiplication        4 Division')
    print('5 Square             6 Power             7 Square Root           8 Inverse')
    print('9 Sin                10 Cos              11 Tan                  12 Switch Sign')
    print('13 invSin            14 invCos           15 invTan               16 Factorial')
    print('17 Log 10            18 10^x             19 Ln                   20 e^x')
    print('21 Log base          22 pi               23 Mole                 24 Random Number')
    print('25 M+                26 MRC              27 MC                   28 Exit')
    print(' ')
    op = int(input('Choose an operation: '))

    memStore = None

    if op == 1:
        print('Addition')
        print('Enter the first addend: ')
        addend1 = enter_num()
        print('Enter the second addend: ')
        addend2 = enter_num()
        result = add(addend1,addend2)
        return result

    elif op == 2:
        print('Subtraction')
        print('Enter the minuend: ')
        minuend = enter_num()
        print('Enter the subtrahend: ')
        subtrahend = enter_num()
        result = subtract(minuend, subtrahend)
        return result

    elif op == 3:
        print('Multiplication')
        print('Enter the first factor: ')
        a = enter_num()
        print('Enter the second factor: ')
        b = enter_num()
        result = multiply(a,b)
        return result

    elif op == 4:
        print('Division')
        print('Enter the dividend: ')
        dividend = enter_num()
        print('Enter the divisor: ')
        divisor = enter_num()
        if divisor == 0:
            print('ERROR')
            return None
        else:
            result = divide(dividend,divisor)
            return result

    elif op == 5:
        print('Square')
        print('Enter a number to square: ')
        base = enter_num()
        result = square(base)
        return result

    elif op == 6:
        print('Power')
        print('Enter the base')
        base = enter_num()
        print('Enter the exponent')
        exponent = enter_num()
        result = exp(base,exponent)
        return result

    elif op == 7:
        print('Square Root')
        print('Enter a radicand: ')
        radicand = enter_num()
        result = square_root(radicand)
        return result

    elif op == 8:
        print('Inverse')
        num = enter_num()
        result = inv(num)
        return result

    elif op == 9:
        print('Sine')
        dr = int(input('Enter 1 for radians and 2 for degrees: '))
        if dr == 1:
            print('Enter an angle in radians to find Sin(angle): ')
            num = enter_num()
            result = sine(num)
            return result
        elif dr == 2:
            print('Enter an angle in degrees to find Sin(angle): ')
            num = enter_num()
            result = sine(math.degrees(num))
            return result

    elif op == 10:
        print('Cosine')
        dr = int(input('Enter 1 for radians and 2 for degrees: '))
        if dr == 1:
            print('Enter an angle in radians to find Cos(angle): ')
            num = enter_num()
            result = cosine(num)
            return result
        elif dr == 2:
            print('Enter an angle in degrees to find Cos(angle): ')
            num = enter_num()
            result = cosine(math.degrees(num))
            return result

    elif op == 11:
        print('Tangent')
        dr = int(input('Enter 1 for radians and 2 for degrees: '))
        if dr == 1:
            print('Enter an angle in radians to find Tan(angle): ')
            num = enter_num()
            result = tangent(num)
            return result
        elif dr == 2:
            print('Enter an angle in degrees to find Tan(angle): ')
            num = enter_num()
            result = tangent(math.degrees(num))
            return result

    elif op == 12:
        print('Switch Sign')
        print("Enter a number to change its sign: ")
        num = enter_num()
        result = switch_sign(num)
        return result

    elif op == 13:
        print('arcSin')
        dr = int(input('Enter 1 for radians and 2 for degrees: '))
        if dr == 1:
            print('Enter an angle in radians to find arcSin(angle): ')
            num = enter_num()
            result = invSin(num)
            return result
        elif dr == 2:
            print('Enter an angle in degrees to find arcSin(angle): ')
            num = enter_num()
            result = invSin(math.degrees(num))
            return result
        elif dr == 2:
            num = input('Enter an angle in degrees to find arcSin(angle): ')
            result = invSin(math.degrees(num))
            return result

    elif op == 14:
        print('arcCos')
        dr = int(input('Enter 1 for radians and 2 for degrees: '))
        if dr == 1:
            print('Enter an angle in radians to find arcCos(angle): ')
            num = enter_num()
            result = invCos(num)
            return result
        elif dr == 2:
            print('Enter an angle in degrees to find arcCos(angle): ')
            num = enter_num()
            result = invCos(math.degrees(num))
            return result
        elif dr == 2:
            num = input('Enter an angle in degrees to find arcCos(angle): ')
            result = invCos(math.degrees(num))
            return result

    elif op == 15:
        print('arcTan')
        dr = int(input('Enter 1 for radians and 2 for degrees: '))
        if dr == 1:
            print('Enter an angle in radians to find arcTan(angle): ')
            num = enter_num()
            result = invTan(num)
            return result
        elif dr == 2:
            print('Enter an angle in degrees to find arcTan(angle): ')
            num = enter_num()
            result = invTan(math.degrees(num))
            return result
        elif dr == 2:
            num = input('Enter an angle in degrees to find arcTan(angle): ')
            result = invTan(math.degrees(num))
            return result

    elif op == 16:
        print('Factorial')
        print('Enter a number to find its factorial: ')
        num = enter_num()
        result = factorial(num)
        return result

    elif op == 17:
        print('Log base 10')
        print('Enter a number to find its log with base 10: ')
        num = enter_num()
        result = log_base_10(num)
        return result

    elif op == 18:
        print('Inverse Log 10^x')
        print('Enter a number to find its inverse log with base 10: ')
        num = enter_num()
        result = inv_log_10(num)
        return result

    elif op == 19:
        print('Log base e, Ln')
        print('Enter a number to find its log with base e: ')
        num = enter_num()
        result = log_base_e(num)
        return result

    elif op == 20:
        print('Inverse log base e, e^x')
        print('Enter a number to find its inverse log with base e: ')
        num = enter_num()
        result = inv_log_e(num)
        return result

    elif op == 21:
        print(' Log of n base b')
        print('Enter a number: ')
        n = enter_num()
        print('Enter a base: ')
        b = enter_num()
        result = log_base_y(n,b)
        return result

    elif op == 22:
        return 3.14159265359

    elif op == 23:
        return 6.02*(10**23)

    elif op == 24:
        rnum = randint(0,100)
        return rnum

    elif op == 25:
        memStore = float(input('Enter a value to store: '))
        print(memStore)
        return memStore

    elif op == 26:
        if type(memStore) != None:
            print(memStore)

    elif op == 27:
        store_choice = input('Do you want to clear memory? Y/N: ').lower()
        if store_choice == 'y':
            memStore = 0
        else:
            pass
        print(memStore)
        return memStore

    elif op == 28:
        condi = False
        print('Goodbye!')


#### Large Loop Functions ####

# Addition

def add(a,b):
    print(a + b)
    return a+b

# Subtraction

def subtract(minuend,subtrahend):
    print(minuend-subtrahend)
    return minuend-subtrahend

# Multiplication

def multiply(a,b):
    print(a*b)
    return a*b

# Division

def divide(dividend,divisor):
    print(dividend/divisor)
    return dividend/divisor

# Square

def square(base):
    print(base ** 2)
    return base ** 2

# Exponent

def exp(base, exponent):
    print(base**exponent)
    return base**exponent

# Square Root

def square_root(n):
    print(n ** (1 / 2))
    return n ** (1 / 2)

# Inverse / Reciprocal

def inv(n):
    print(1/n)
    return 1/n

#### Trig

def sine(x):
    print(math.sin(x))
    return math.sin(x)

def cosine(x):
    print(math.cos(x))
    return math.cos(x)

def tangent(x):
    print(math.tan(x))
    return math.tan(x)

def invSin(x):
    print(math.asin(x))
    return math.asin(x)

def invCos(x):
    print(math.acos(x))
    return math.acos(x)

def invTan(x):
    print(math.atan(x))
    return math.atan(x)

# Switch Sign

def switch_sign(n):
    print(-1*n)
    return -1 * n

# Factorial

def factorial(n):
    print(math.factorial(n))
    return math.factorial(n)

# Log Base 10

def log_base_10(n):
    print(math.log10(n))
    return math.log10(n)

# Inverse log 10^x

def inv_log_10(n):
    print(10**n)
    return 10**n

# Log Base e

def log_base_e(n):
    print(math.log(n))
    return math.log(n)

# Inverse ln

def inv_log_e(n):
    print(math.exp(n))
    return math.exp(n)

# Log Base Custom

def log_base_y(n, base):
    print(math.log(n, base))
    return math.log(n, base)

def choose_data_type():
    data_choice = int(input('Enter data type: 1. Decimal 2. Hexadecimal 3. Binary 4. Octal '))
    if data_choice == 1:
        print(main_result)
        return main_result
    elif data_choice == 2:
        print(hex(int(main_result)))
        return hex(int(main_result))
    elif data_choice == 3:
        print(bin(int(main_result)).replace("0b", ""))
        return bin(int(main_result)).replace("0b", "")
    elif data_choice == 4:
        print(oct(int(main_result)))
        return oct(int(main_result))


#### Small Loop ####

def choose_small_op():
    print('1 Addition           2 Subtraction       3 Multiplication        4 Division')
    print('5 Square             6 Power             7 Square Root           8 Inverse')
    print('9 M+                 10 MRC              11 MC                   12 Exit')
    print(' ')
    op = int(input('Choose an operation: '))

    memStore = None

    if op == 1:
        print('Addition')
        print('Enter the second addend: ')
        addend2 = enter_num()
        result = add2(addend2)
        return result

    elif op == 2:
        print('Subtraction')
        print('Enter the subtrahend: ')
        subtrahend = enter_num()
        result = subtract2(subtrahend)
        return result

    elif op == 3:
        print('Multiplication')
        print('Enter the second factor: ')
        b = enter_num()
        result = multiply2(b)
        return result

    elif op == 4:
        print('Division')
        print('Enter the divisor: ')
        divisor = enter_num()
        result = divide2(divisor)
        return result

    elif op == 5:
        print('Square')
        result = square2(main_result)
        return result

    elif op == 6:
        print('Power')
        print('Enter the exponent')
        exponent = enter_num()
        result = exp2(exponent)
        return result

    elif op == 7:
        print('Square Root')
        result = square_root2(main_result)
        return result

    elif op == 8:
        print('Inverse')
        #num = enter_num()
        result = inv2(main_result)
        return result

    elif op == 9:
        memStore = main_result
        print(memStore)
        return memStore

    elif op == 10:
        if type(memStore) != None:
            print(memStore)
        else:
            print('Empty')

    elif op == 11:
        store_choice = input('Do you want to clear memory? Y/N: ').lower()
        if store_choice == 'y':
            memStore = 0
        else:
            pass
        print(memStore)
        return memStore

    elif op == 12:
        condi = False
        print('Goodbye!')
        