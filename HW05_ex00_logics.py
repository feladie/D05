#!/usr/bin/env python3
# HW05_ex00_logics.py


##############################################################################
def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """
    try:
        user_input = int(input('Enter an integer: '))
        if user_input % 2 == 0:
            print('even')
        else:
            print('odd')
    except:
        print('Please try again. Enter an integer.')
        return even_odd()


def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    for row_number in range(0, 10):
        for column_number in range(1, 10):
            number = column_number + (row_number * 10)
            print("{:<5}".format(number), end = " ")
        print("{:<5}".format(10 + (row_number * 10)))

def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    user_input = ''
    sum = 0
    count = 0

    while (user_input != 'done'):
        user_input = input('number: ')
        if (user_input == 'done') and (count == 0): # user enters 'done' as first input
            return None            
        elif (user_input == 'done') and (count > 0): # user enters done after entering numbers
            return sum / count
        else:   # user inputs a number to add to the average
            try:
                sum += float(user_input)
                count += 1
            except: # user enters input other than a number or 'done'
                print('Please type a number.')
                return find_average()

##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    # even_odd()
    # ten_by_ten()
    find_average()

if __name__ == '__main__':
    main()
