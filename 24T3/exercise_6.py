# You can assume that word_pairs() is called with a string of
# uppercase letters as agument.
#
# dictionary.txt is stored in the working directory.
#
# Outputs all pairs of distinct words in the dictionary file, if any,
# that are made up of all letters in available_letters
# (if a letter in available_letters has n occurrences,
# then there are n occurrences of that letter in the combination
# of both words that make up an output pair).
#
# The second word in a pair comes lexicographically after the first word.
# The first words in the pairs are output in lexicographic order
# and for a given first word, the second words are output in
# lexicographic order.
#
# Hint: If you do not know the imported Counter class,
#       experiment with it, passing a string as argument, and try
#       arithmetic and comparison operators on Counter objects.


from collections import Counter
from collections import defaultdict

dictionary_file = 'dictionary.txt'


def word_pairs(available_letters):
    '''
    >>> word_pairs('ABCDEFGHIJK')
    >>> word_pairs('ABCDEF')
    CAB FED
    >>> word_pairs('ABCABC')
    >>> word_pairs('EOZNZOE')
    OOZE ZEN
    ZOE ZONE
    >>> word_pairs('AIRANPDLER')
    ADRENAL RIP
    ANDRE APRIL
    APRIL ARDEN
    ARID PLANER
    ARLEN RAPID
    DANIEL PARR
    DAR PLAINER
    DARER PLAIN
    DARNER PAIL
    DARPA LINER
    DENIAL PARR
    DIRE PLANAR
    DRAIN PALER
    DRAIN PEARL
    DRAINER LAP
    DRAINER PAL
    DRAPER LAIN
    DRAPER NAIL
    ERRAND PAIL
    IRELAND PAR
    IRELAND RAP
    LAIR PANDER
    LAND RAPIER
    LAND REPAIR
    LANDER PAIR
    LARDER PAIN
    LEARN RAPID
    LIAR PANDER
    LINDA RAPER
    NADIR PALER
    NADIR PEARL
    NAILED PARR
    PANDER RAIL
    PLAN RAIDER
    PLANAR REID
    PLANAR RIDE
    PLANER RAID
    RAPID RENAL
    '''
    words = defaultdict(list)
    with open(dictionary_file) as file:
        for line in file:
            word = line.strip()
            if word:
                words[len(word)].append(word)
    length = len(available_letters)
    avail_counter = Counter(available_letters)
    pairs = set()
    for i in range(1, length//2+1):
        for w1 in words[i]:
            w1_counter = Counter(w1)
            if not w1_counter - avail_counter:
                for w2 in words[length-i]:
                    if w2 == w1: continue
                    w2_counter = Counter(w2)
                    if not w2_counter - (avail_counter - w1_counter):
                        pairs.add(tuple(sorted([w1,w2])))
    pairs = sorted(list(pairs))
    for w1, w2 in pairs:
        print(w1, w2)
    # REPLACE PASS ABOVE WITH YOUR CODE


# word_pairs('EOZNZOE')
if __name__ == '__main__':
    import doctest
    doctest.testmod()
