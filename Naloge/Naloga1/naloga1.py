__author__ = 'Janko'
# program poisce vse veckratnike stevil 3 in 5 do stevila 1000
# in vrne vsoto vseh veckratnikov

datoteka = "log.txt"
WRITE = "w"
APPEND = "a"
# spremenljivka za racunanje vsote
total = 0
# poisce vse veckratnike  sproti sesteva in shrani v datoteko
openFile = open(datoteka,WRITE)
print("Datoteka z imenom %s je bila ustvarjena!" %(datoteka))
openFile.close()

with open(datoteka, APPEND)as log:
    log.write("V datoteki so zapisani vsi veckratniki stevila 3 in 5 med 1 in 1000\n")
    for n in range(1,1000):
        if n % 3 == 0 or n % 5 == 0:
            log.write(str(n)+"\n")
            total += n
            print(n)
print("Datoteka %s je bila uspesno zapisana!" %(datoteka))
print("Vsota vseh veckratnikov stevila tri in 5 od 1 do 1000 je: %d" %(total))