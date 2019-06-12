from numpy import random

def roll(num_sides):
    try:
        num_sides_int = int(num_sides)
    except ValueError:
        return 'Please enter an integer.'
    if num_sides_int <= 0:
        return 'Please enter an integer greater than 0.'
    elif num_sides_int != float(num_sides):
        return 'Please enter an integer.'
    else:
        result = random.randint(1,num_sides_int+1)
        return result

if __name__ == '__main__':
    result = roll(input("Enter the number of sides: "))
    print(result)
