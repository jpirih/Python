# user enters number and program pritns all the divisors of the number

number = int(raw_input("Enter a number: "))
divisors_range = range(1,number+1)

divisors = []

for n in divisors_range:
    if number % n == 0:
        divisors.append(n)

print("All divisors of %d are:" %number)
print(divisors)