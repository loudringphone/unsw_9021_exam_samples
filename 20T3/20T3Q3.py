# Final Exam - Question 3

# ord(c) returns the encoding of character c.
# chr(e) returns the character encoded by e.


def f(width, height):
    
    '''
    Displays a rectangle by outputting lowercase letters, starting with a,
    in a "snakelike" manner, from left to right, then from right to left,
    then from left to right, then from right to left, wrapping around when
    z is reached.

    You can assume that width and height are strictly positive integers
    
    >>> f(1, 1)
    a
    >>> f(2, 3)
    ab
    dc
    ef
    >>> f(3, 2)
    abc
    fed
    >>> f(17, 4)
    abcdefghijklmnopq
    hgfedcbazyxwvutsr
    ijklmnopqrstuvwxy
    ponmlkjihgfedcbaz
    '''
    # ord('a') = 97; ord('z') = 122
    to_right = True
    chr_ord = 97
    for _ in range(height):
        string = ''
        if to_right:
            for _ in range(width):
                string += chr(chr_ord)
                chr_ord += 1
        else:
            for _ in range(width):
                string = chr(chr_ord) + string
                chr_ord += 1
                if chr_ord == 123: chr_ord = 97
        to_right = not to_right
        print(string)
    # INSERT YOUR CODE HERE

# f(17, 4)
if __name__ == '__main__':
    import doctest
    doctest.testmod()


