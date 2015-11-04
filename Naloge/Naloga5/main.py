__author__ = 'Janko'
while True:
    stevilo = int (raw_input("Vnesi stevilo med 0 in 100: "))
    if stevilo > 0 and stevilo <= 100:
        for n in range(1, stevilo + 1):
            if n % 3 == 0 and n % 5 != 0:
                print("fizz")
                continue
            elif n % 5 == 0 and n %3 != 0:
                print("buzz")
                continue
            elif(n % 3 == 0) and (n % 5 == 0):
                print("fizzbuzz")
                continue
            print(n)
        break
    else:
        print("Prosim vnesi stevilo med 0 in 100")
