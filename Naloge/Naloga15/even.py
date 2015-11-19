# Write one line of Python that takes this list a and makes a new list that has only the even
# data
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# list that contains only even numbers from a list
even_list = [x for x in a if x % 2 == 0]
print(even_list)