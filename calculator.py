#### Small Functions ####

# Addition

def add2(b):
    print(main_result+b)
    return main_result+b

# Subtraction

def subtract2(subtrahend):
    print(main_result-subtrahend)
    return main_result-subtrahend

# Multiplication

def multiply2(b):
    print(main_result*b)
    return main_result*b

# Division

def divide2(divisor):
    print(main_result/divisor)
    return main_result/divisor

# Square

def square2(base):
    print(main_result ** 2)
    return main_result ** 2

# Exponent

def exp2(exponent):
    print(main_result**exponent)
    return main_result**exponent

# Square Root

def square_root2(main_result):
    print(main_result ** (1 / 2))
    return main_result ** (1 / 2)

# Inverse / Reciprocal

def inv2(main_result):
    print(1/main_result)
    return 1/main_result

print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')

#### Program ####
print('Welcome to the Python Scientific Calculator.')

condi = True
while condi:
    main_result = choose_op()
    print(f'Result: {main_result}')
    choose_data_type()
    print('')
    cont = input('Continue with current value Y/N? \n'
                 'Warning: N clears the display: ').lower()
    print('')
    if cont == 'y':
        condi2 = True
        while condi2:
            main_result = choose_small_op()
            print(f'Result: {main_result}')
            choose_data_type()
            print('')
            cont2 = input('Continue with current value Y/N?\n'
                          'Warning: N clears the display: ').lower()
            print('')
            if cont2 == 'y':
                condi2 = True
            else:
                break
    #else:
        #condi = False
        #print('Goodbye!')
