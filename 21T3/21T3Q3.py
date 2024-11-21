'''
You might find the ord() function useful.
'''
def longest_leftmost_sequence_of_consecutive_letters(word):
    '''
    You can assume that "word" is a string of nothing but lowercase letters.
    
    >>> longest_leftmost_sequence_of_consecutive_letters('')
    ''
    >>> longest_leftmost_sequence_of_consecutive_letters('a')
    'a'
    >>> longest_leftmost_sequence_of_consecutive_letters('zuba')
    'z'
    >>> longest_leftmost_sequence_of_consecutive_letters('ab')
    'ab'
    >>> longest_leftmost_sequence_of_consecutive_letters('bcab')
    'bc'
    >>> longest_leftmost_sequence_of_consecutive_letters('aefbxyzcrsdt')
    'xyz'
    >>> longest_leftmost_sequence_of_consecutive_letters('efghuvwrstuvabcde')
    'rstuv'
    '''

    # ord('a') = 97; ord('z') = 122
    if not len(word): return ''
    seq = longest_seq = word[0]
    for i in range(1, len(word)):
        cur_ord = ord(word[i]); last_ord = ord(word[i-1])
        if (cur_ord == 97 and last_ord == 122) or cur_ord - last_ord == 1:
            seq += word[i]
        else:
            if len(seq) > len(longest_seq):
                longest_seq = seq
            seq = word[i]
    if len(seq) > len(longest_seq):
        longest_seq = seq
    return longest_seq
    # REPLACE return WITH YOUR CODE


# longest_leftmost_sequence_of_consecutive_letters('ab')
if __name__ == '__main__':
    import doctest
    doctest.testmod()

