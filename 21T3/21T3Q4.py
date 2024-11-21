# COMP9021 21T3 - Rachid Hamadi
# Final Exam Question 4

'''
No point to hard code for small values of n, will be tested
only for large enough values...
'''

def pascal_triangle_line(n):
    '''
    Recall: it is the list of binomial coefficients that give the
    number of ways of choosing k objects out of n - 1 for 0 <= k < n.

    >>> pascal_triangle_line(1)
    [1]
    >>> pascal_triangle_line(2)
    [1, 1]
    >>> pascal_triangle_line(3)
    [1, 2, 1]
    >>> pascal_triangle_line(4)
    [1, 3, 3, 1]
    >>> pascal_triangle_line(5)
    [1, 4, 6, 4, 1]
    >>> pascal_triangle_line(6)
    [1, 5, 10, 10, 5, 1]
    >>> pascal_triangle_line(7)
    [1, 6, 15, 20, 15, 6, 1]
    >>> pascal_triangle_line(8)
    [1, 7, 21, 35, 35, 21, 7, 1]
    '''
    if n == 1: return [1]
    old_list = [1,1]
    if n == 2: return old_list
    for _ in range(3, n+1):
        new_list = [1]
        for j in range(1, len(old_list)):
            prev_num = old_list[j-1]
            curr_num = old_list[j]
            new_list.append(prev_num+curr_num)
        new_list.append(1)
        old_list = new_list.copy()
    return new_list
    # REPLACE return WITH YOUR CODE
    

# pascal_triangle_line(3)
if __name__ == '__main__':
    import doctest
    doctest.testmod()

