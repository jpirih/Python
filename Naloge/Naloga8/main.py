import datetime
# program vprasa uporabnika za ime in starost
# izpise pozdrav in uporabniku pove katerega leta bo dopolnil 100 let

name = raw_input("Prosim vnesi ime: ")
age = raw_input("Prosim vnesi starost v letih: ")
age = int(age)

print("Zdravo %s star/-a si %d let" %(name,age))

datum = datetime.datetime.today()
letos = datum.year
stoLet = letos + (100 - age)
print("Sto let bos star/-a  leta %d"%(stoLet))
