# Final Exam Question 8
from collections import defaultdict
def is_heterosquare(square):
    '''
    A heterosquare of order n is an arrangement of the integers 1 to n**2 in a square,
    such that the rows, columns, and diagonals all sum to DIFFERENT values.
    In contrast, magic squares have all these sums equal.
    
    Conjunctions of inputs will be tested, so hard coding will not help.
    
    >>> is_heterosquare([[1, 2, 3],\
                         [8, 9, 4],\
                         [7, 6, 5]])
    True
    >>> is_heterosquare([[1, 2, 3],\
                         [9, 8, 4],\
                         [7, 6, 5]])
    False
    >>> is_heterosquare([[2, 1, 3, 4],\
                         [5, 6, 7, 8],\
                         [9, 10, 11, 12],\
                         [13, 14, 15, 16]])
    True
    >>> is_heterosquare([[1, 2, 3, 4],\
                         [5, 6, 7, 8],\
                         [9, 10, 11, 12],\
                         [13, 14, 15, 16]])
    False
    '''
    height = len(square)
    if not height: return False
    width = len(square[0])
    if not width: return False
    values = []
    for row in square:
        values.append(sum(row))
    for col in list(zip(*square)):
        values.append(sum(col))
    val = 0
    for j in range(width):
        val += square[j][j]
    values.append(val)
    val = 0; i = 0
    for j in range(width-1, -1, -1):
        val += square[i][j]
        i += 1
    values.append(val)
    counter = defaultdict(int)
    for val in values:
        counter[val] += 1
        if counter[val] > 1:
            return False
    return True
    # REPLACE return WITH YOUR CODE


# POSSIBLY DEFINE OTHER FUNCTIONS

if __name__ == '__main__':
    import doctest
    doctest.testmod()
