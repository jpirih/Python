__author__ = 'Janko'
# to je enostavni kalkulator



rezultat = 0
try:
    n1 = float(raw_input("Vnesi stevilo: "))
    oper = raw_input("Vnesi operacijo (+ - *  /): ")
    n2 = float(raw_input("Vnesi drugo stevilo: "))

    if oper == "+":
        rezultat = n1 + n2
        print(rezultat)
    elif oper == "-":
        rezultat = n1 - n2
        print(rezultat)
    elif oper == "*":
        rezultat = n1 * n2
        print(rezultat)
    elif oper == "/":
        rezultat = n1 / n2
        print(rezultat)
    else:
        print("Prosim vnesi eno od dovoljenih operacij + - * /")
except ValueError:
    print("prosim vnesi stevilo")
except ZeroDivisionError:
    print("Deljenje z 0 ni dovoljeno!")

