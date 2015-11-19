# -*- coding: utf-8 -*-
import datetime
import csv
# program omoca, da uporabni dodaja izdelke na nakupovalni listek

#funcija bere datoteko v kateri so zabelezeni vsi dosedaj shranjeni listki
def readFiles(datoteka):
    with open(datoteka, "r") as openedFile:
        print(openedFile.read())

#datum in cas  se uporablja v imenu datoteke, da se medsabo razlikujejo
#datum cas v iso formatu brez locilnih znakov
danes = datetime.datetime.today()
datum = datetime.datetime.strftime(danes, "%Y%m%dT%H%M%S")
datum = str(datum)

# prazen seznam nakupovalni listek
lisek = []
logName = "shranjeniListki.txt"
# za delo za datotekami ustavanjane datoreke za nov  nakupovalni listek
fileName = "listek-%s.txt" %(datum)
WRITE = "w"
APPEND = "a"
READ = "r"

#-----------------PREGLED SHRANJENIH LISTKOV--------------------------------------
shranjeniListki = []
logR = open(logName, READ)
logRVsebina = csv.reader(logR)
print("Trenutno so shranjeni naslednji listki:")
for line in logRVsebina:
    shranjeniListki.append(line[0])
logR.close()

print("izberi eno do moznosti: ")
print("n - nov nakupovalni listek \nu - urejanje shranjenih listkov \np - pregled shranjenih listkov")
akcija = raw_input("Vnesi eno od nastetih moznosti n, p, u: ")
print(" ")

#-----------------USTVARI NOV NAKUPOVALNI LISTEK--------------------------------------
if akcija == "n":
    #zapisuje zgodovino shranjenih listkov - mozno kasnejse urejanje
    log = open(logName, APPEND)
    log.write(fileName + "\n")
    log.close()

    novListek = open(fileName, WRITE)
    while True:
        dodaj = raw_input("Ali zelis dodati nov izdelek na nakupovalni listek ? (da/ne): ")
        # dodajanje izdelkov na nov listek
        if dodaj == "da":
            izdelek = raw_input("Napisi izdelek, ki ga zelis dodati na listek: ")
            # preverja podvajanje elementov na nakupovalnem listku
            if izdelek in lisek:
                print("%s je ze na nakupovalnem listku" %(izdelek))
                izdelek = raw_input("Vpisi drug izdelek: ")
                lisek.append(izdelek)
                novListek.write(izdelek + "\n")
            else:
                lisek.append(izdelek)
                novListek.write(izdelek + "\n")
        elif dodaj == "ne":
            print(" ")
            print("Dodajanje izdelkov na listek je koncno ")
            print("datoteka z imenom %s je bila uspesno kreirana" %(fileName))
            novListek.close()
            break
        else:
            print("Zelis dodati izdelek vpisi da ali ne: ")
    print(" ")
    #izpis nakupovalnega listka v konzolo
    print("Tvoj listek vsebuje naseldnje izdelke:")
    # izpse izdelke na sseznamu
    for i in lisek:
        print(i)
#------------UREJANJE LISTKOV -dodajanje na obstojece listke--------
elif akcija == "u":
    print("Tretutno so shranjeni naslednji listki:")
    print(shranjeniListki)
    listekID = int(raw_input("Za urejanje prvega napiši 0 drugi =1, 2 ,3...: "))
    print(" ")
    print("izbran nakupovalni listek %s trenutno vsebuje naslednje izdelke: " %shranjeniListki[listekID])
    readFiles(str(shranjeniListki[listekID]))
    print(" ")
    with open(shranjeniListki[listekID], APPEND) as urediListek:
        while True:
            dodaj = raw_input("Dodaj nov izdelek da/ne: ")
            if dodaj == "da":
                izdelek =raw_input("Vpisi izdelek, ki ga zelis dodati: ")
                urediListek.write(izdelek+"\n")
            elif dodaj == "ne":
                print("Torej si dodal ze vse izdelke")
                break
    print(" ")
    print("Nov in dopolnjen listek %s zdaj izgleda takole:" %shranjeniListki[listekID])
    readFiles(str(shranjeniListki[listekID]))

#-----------------PREGLED SHRANJENIH LISTKOV--------------------------------------
elif akcija == "p":
    print("Trenutno so shranjeni naslednji listki:")
    print(shranjeniListki)
else:
    print("vpisi n, p ali u")





