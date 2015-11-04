__author__ = 'Janko'
import random

skritoStevilo = random.randrange(1,10)
stevec = 0
print("ugani skrito stevilo ")
while True:
    try:
        vnesenoStevilo = input("Vpisi stevilo med 1 in 10 ")
        stevec +=1
        if vnesenoStevilo == skritoStevilo:
            print("Baravo uganil si skrito stevilo je %d" %(skritoStevilo))
            print("Za ugibanje si porabil %d poskusov" %(stevec))
            break
        else:
            print("Vpisal si %d to zal ni skrito stevilo. Poskusi znova" %(vnesenoStevilo))
    except NameError:
        print("Prosim vpisi stevilo")