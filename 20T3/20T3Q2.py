# Final Exam - Question 2

def filtered_sequence(L, n):
    '''
    Returns a list LL that keeps from L all elements e
    that are part of a sub-sequence of length at least n.

    All elements of the sub-sequence have the same value as e.

    You can assume that L is a list of valid integers.

    >>> filtered_sequence([], 2)
    []
    >>> filtered_sequence([7], 0)
    [7]
    >>> filtered_sequence([7], 1)
    [7]
    >>> filtered_sequence([7], 2)
    []
    >>> filtered_sequence([1, 3, 1, 2, 5, 6, 8, 2], 1)
    [1, 3, 1, 2, 5, 6, 8, 2]
    >>> filtered_sequence([1, 3, 3, 3, 2, 4, 4, 5, 6, 6, 6, 6], 2)
    [3, 3, 3, 4, 4, 6, 6, 6, 6]
    >>> filtered_sequence([7, 7, 7, 7, 2, 2, 7, 3, 4, 4, 4, 6, 5], 3)
    [7, 7, 7, 7, 4, 4, 4]
    >>> filtered_sequence([1, 1, 1, 1, 5, 5, 1, 1, 1, 1, 5, 5, 5, 5, 5, 6], 4)
    [1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5]
    '''

    LL = []
    if not L: return LL

    curr_num = L[0]
    seq = []
    for num in L:
        if num == curr_num:
            seq.append(num)
        else:
            if len(seq) >= n:
                LL += seq
            seq = [num]
            curr_num = num
    if len(seq) >= n:
        LL += seq
    return LL
    # INSERT YOUR CODE HERE


# filtered_sequence([1, 1, 1, 1, 5, 5, 1, 1, 1, 1, 5, 5, 5, 5, 5, 6], 4)
if __name__ == '__main__':
    import doctest
    doctest.testmod()