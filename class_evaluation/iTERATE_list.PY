list1 = [1, 2, 3]
list2 = ['p', 'q', 'r']


# Using zip () to iterate over multiple lists simultaneously
for i1, i2 in zip(list1, list2):
    print(f' {i1} -> {i2}')