def has_duplicates(sequence):
    seen = set()                # Create an empty set to store elements we've already seen
    for element in sequence:    # Loop through each element in the input sequence
        if element in seen:     # Check if the current element is already in the 'seen' set
            return True         # If yes, we found a duplicate, so return True immediately
        seen.add(element)       # If not a duplicate, add the current element to the 'seen' set
    return False

print(has_duplicates('dermatoglyphics'))  # False
print(has_duplicates('unpredictably'))    # False
print(has_duplicates('brontosaurus'))     # True (has duplicate 'o', 'r', 's', 'u')

