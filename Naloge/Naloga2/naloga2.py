__author__ = 'Janko'
# program sesteva sode clene fibbonacijevega zaporedja
# dokler vsota <= 4 mio in vrne vsoto teh clenov
number = 1
last = 0
beforeLast = 0

total = 0
file = "fibbo.txt"
WRITE = "w"

log = open(file,WRITE)
log.write("fibbonaccijevo zaporedje \n")
while True:
    beforeLast = last
    last = number
    number = beforeLast + last
    log.write(str(number)+"\n")
    print(number)

    if number % 2 == 0:
        total += number
    elif total >= 4000000:
        break

print("datoteka je bila uspesno zapisana")
log.close()
print("Vsota sodih clenov zaporedja znasa: %d"%(total))

