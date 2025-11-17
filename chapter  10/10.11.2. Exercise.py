#10.11.2. Exercise

#counter = value_counts('brontosaurus')

# Version 1
def value_counts(string):
    counter = {}
    for letter in string:
        if letter not in counter:                       # if letter is not in the dictionary, we create a new item with key letter and value 1
            counter[letter] = 1
        else:
            counter[letter] += 1                        # if letter is already in the dictionary we increment the value associated with letter.
    return counter



#Version 2

def value_counts(string):
      counter = {}
      for letter in string:                              # we add 1 to this value
          counter[letter] = counter.get(letter, 0) + 1   # returns the current count if letter exists in the dictionary, or 0 if it doesn't
      return counter                                     # we assign the result back to counter[letter]


counter = value_counts('brontosaurus')
print(value_counts('brontosaurus')
