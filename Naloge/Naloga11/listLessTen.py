# Naloga v txt datoteki

# podatki

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# program prints out all the numbers in the a list that are less then 5
for item in a:
    if item < 5:
        print(item)

# create new list with elements less than 5
less_than_five = []
for i in a:
    if i < 5:
        less_than_five.append(i)
print(less_than_five)

# all in one line
print(filter(lambda x:x < 5,a))

# ask the user for the number nad return a list of numbers that are smaller then the number
number = int(raw_input("Enter the number less than 89: "))

elements_smaller_than_number = []
for n in a:
    if n < number:
        elements_smaller_than_number.append(n)

print("elements from the orignial a list that are smaller that %d are:" %number)
print(elements_smaller_than_number)
