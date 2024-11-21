# Final Exam - Question 1

def average_of_digits_common_to(*numbers):
    '''
    If there are no numbers, or if the numbers have no digits in common,
    then returns -1.
    Else, returns the average of the digits common to all numbers
    (each common digit being counted only once).

    You can assume that numbers are all valid non-negative integers.

    >>> average_of_digits_common_to()
    -1
    >>> average_of_digits_common_to(0, 12, 456)
    -1
    >>> average_of_digits_common_to(223444)\
#             (2 + 3 + 4) / 3 == 3.0
    3.0
    >>> average_of_digits_common_to(135, 567)\
#             5 / 1 == 5.0
    5.0
    >>> average_of_digits_common_to(234, 345, 2345, 3456, 112233445566)\
#             (3 + 4) / 2 == 3.5
    3.5
    >>> average_of_digits_common_to(932932, 139139, 395395395)\
#             (3 + 9) / 2 == 6.0
    6.0
    >>> average_of_digits_common_to(3136823, 665537857, 8363265, 35652385)\
#             (3 + 6 + 8) / 3 == 5.666666666666667
    5.666666666666667
    '''
    if not numbers: return -1

    strings = [str(num) for num in numbers]
    common_nbs = []
    for num in range(10):
        is_common = True
        for string in strings:
            if str(num) not in string:
                is_common = False
        if is_common:
            common_nbs.append(num)
    if not common_nbs:
        return -1
    else:
        return sum(common_nbs)/len(common_nbs)
    # return
    # REPLACE "return" ABOVE WITH YOUR CODE

# average_of_digits_common_to(0, 12, 456)
if __name__ == '__main__':
    import doctest
    doctest.testmod()
