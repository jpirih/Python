__author__ = 'Janko'
# program razcleni dano stevilo na prafaktorje in pove kateri je
# najvecji med njimi

number = 600851475143
i = 2

while  i * i < number:
    while number % i == 0:
        number = number /i
        print(i)
    i = i + 1
print(number)


