def do_square(number):
    return number * number


def do_factorial(number):
    if(number < 0 ):
        return 0
    if(number == 1):
        return number
    return number * do_factorial(number - 1);