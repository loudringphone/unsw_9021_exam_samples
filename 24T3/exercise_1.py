# Note that NONE OF THE LINES THAT ARE OUTPUT HAS TRAILING SPACES.
#
# You can assume that vertical_bars() is called with nothing but
# integers at least equal to 0 as arguments (if any).


def vertical_bars(*x):
    '''
    >>> vertical_bars()
    >>> vertical_bars(0, 0, 0)
    >>> vertical_bars(4)
    *
    *
    *
    *
    >>> vertical_bars(4, 4, 4)
    * * *
    * * *
    * * *
    * * *
    >>> vertical_bars(4, 0, 3, 1)
    *
    *   *
    *   *
    *   * *
    >>> vertical_bars(0, 1, 2, 3, 2, 1, 0, 0)
          *
        * * *
      * * * * *
    '''
    if not x: return
    max_height = max(x)
    while max_height:
        str = ''
        for i in x:
            if i >= max_height:
                str += '* '
            else:
                str += '  '
        print(str.rstrip())
        max_height -= 1
    # REPLACE PASS ABOVE WITH YOUR CODE

# vertical_bars(0, 1, 2, 3, 2, 1, 0, 0)
if __name__ == '__main__':
    import doctest
    doctest.testmod()
