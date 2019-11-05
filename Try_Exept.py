def concatenating():
    x = input('Enter first value:')
    y = input('Enter second value:')
    try:
        # x = float(x)
        # y = float(y)
        print(int(x) + int(y))
    except ValueError:
        print(str(x) + str(y))
    finally:
        print("Happy day!")

concatenating()

def divide():
    a = float(input('Enter first value:'))
    b = float(input('Enter second value:'))

    try:
        print(int(a) / int(b))
    except ZeroDivisionError:
        print('You divide on zero')
    finally:
        print("the end")


divide()
