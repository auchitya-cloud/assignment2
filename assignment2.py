# 1. Write a python program to sort the list of heterogeneous data.
# e.g.
# L = ["Ram", 1, "Shyam", 2, "Aman", 3]
# print(L)
# L.sort()
# print(L)
# Above code gives error. Correct it
L = ["Ram", 1, "Shyam", 2, "Aman", 3]

# Separate integers and strings into two lists
integers = [item for item in L if isinstance(item, int)]
strings = [item for item in L if isinstance(item, str)]

# Sort the lists
integers.sort()
strings.sort()

# Merge the sorted lists back together
sorted_list = []
for item in L:
    if isinstance(item, int):
        sorted_list.append(integers.pop(0))
    else:
        sorted_list.append(strings.pop(0))

print(sorted_list)
