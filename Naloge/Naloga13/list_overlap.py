# program returns a list of numbers that are comon to both lists a and b

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
comon_numbers = []

for stevA in a:
    if stevA in comon_numbers:
        None
    elif stevA in b:
        comon_numbers.append(stevA)

print(comon_numbers)

# same code in one line
# filters the b - longer list and prints out only the numbers from b that are comon in list a
print(filter(lambda x: x in a,b))
