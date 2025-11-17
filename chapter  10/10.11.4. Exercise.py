from pandas import value_counts


def find_repeats(counter):
    """Makes a list of keys with values greater than 1.

    counter: dictionary that maps from keys to counts

    returns: list of keys
    """
    repeats = []                        #  Create an empty list to store keys with counts > 1
    for key in counter:
        if counter[key] > 1:            #  Loop through each key in the dictionary.
            repeats.append(key)         #  If the value associated with that key is greater than 1, add the key to the list
    return repeats                      #  Return the list of repeated keys

counter = value_counts('brontosaurus')
print(counter)

repeats = find_repeats(counter)
print(repeats)