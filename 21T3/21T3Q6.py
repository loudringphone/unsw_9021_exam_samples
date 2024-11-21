# Final Exam Question 6

def statistics(filename):
    '''
    A text file, stored in the working directory, consists of sentences.
    A sentence consists of words, possibly directly followed by a comma,
    except for the last word which is directly followed by a full stop.
    Words are separated by spaces.

    >>> statistics('text_file_1.txt')
    There are 2 sentence(s).
    The shortest sentence has 31 word(s).
    The longest sentence has 34 word(s).
    The shortest word has 1 character(s).
    The longest word has 9 character(s).
    >>> statistics('text_file_2.txt')
    There are 4 sentence(s).
    The shortest sentence has 6 word(s).
    The longest sentence has 34 word(s).
    The shortest word has 1 character(s).
    The longest word has 12 character(s).
    >>> statistics('text_file_3.txt')
    There are 1 sentence(s).
    The shortest sentence has 30 word(s).
    The longest sentence has 30 word(s).
    The shortest word has 1 character(s).
    The longest word has 12 character(s).
    '''
    sentence_nb = 0
    shortest_sentence = float('inf')
    shortest_word = float('inf')
    longest_sentence = float('-inf')
    longest_word = float('-inf')
    with open(filename) as file:
        content = [sentence for sentence in file.read().split('.') if sentence]
        sentence_nb = len(content)
        for i in range(len(content)):
            content[i] = content[i].split(' ')
            j = 0
            while not j == len(content[i]):
                word = content[i][j]
                if not word:
                    content[i].pop(j)
                else:
                    word_len = len(word)
                    if word_len > longest_word:
                        longest_word = word_len
                    if word_len < shortest_word:
                        shortest_word = word_len
                    j += 1
            sentence_len = len(content[i])
            if sentence_len > longest_sentence:
                longest_sentence = sentence_len
            if sentence_len < shortest_sentence:
                shortest_sentence = sentence_len
    print(f'There are {sentence_nb} sentence(s).')
    print(f'The shortest sentence has {shortest_sentence} word(s).')
    print(f'The longest sentence has {longest_sentence} word(s).')
    print(f'The shortest word has {shortest_word} character(s).')
    print(f'The longest word has {longest_word} character(s).')
    
    
    
    
    


statistics('text_file_1.txt')
# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()

