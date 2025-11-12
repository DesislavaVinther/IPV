letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = range(len(letters))
letter_map = dict(zip(letters, numbers))


#   Encodes a word using Caesar cipher by shifting each letter.
#       word: string (lowercase letters)
#       shift: integer (number of positions to shift)
#       returns: string (encoded word)

def shift_word(word, shift):
    #shifted_letters = []                 # Probably an overkill with a list
    output = ''

    for letter in word:
        index = letter_map[letter]                  # Find the index of the current letter i alfabetet

        new_index = (index + shift) % 26            # Shift it and wrap around using modulus 26

        new_letter = letters[new_index]             # Get the new letter at the shifted position

        output = output+new_letter                   # Add to our result list

    return output                                      # Join all letters into a string

print(shift_word('cubed',10))