list0 = [1, 2, 3]
list1 = [4, 5]

t = (list0, list1)

t[1].append(6)                  # the contents of the mutable objects inside the tuple can still be modified
print(t)                        # So t[1] still refers to the same list object, but we CAN modify that list

d = {t: 'this tuple contains two lists'}        # This fails because: # 1) Dictionary keys must be hashable
                                                                      # 2) An object is hashable only if its hash value never changes during its lifetime
                                                                      # 3) Since the lists inside t can be modified, Python can't compute a stable hash for the tuple
                                                                      # 4) Therefore, t cannot be used as a dictionary key

#   Tuples are only hashable if all their elements are hashable.
#   A tuple containing mutable objects (lists, dicts, sets) is not hashable, even though the tuple itself is immutable.