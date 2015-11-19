# -*- coding: utf-8 -*-
# program omoca, da uporabni dodaja izdelke na nakupovalni listek

# prazen seznam nakupovalni listek
lisek = []

while True:
    dodaj = raw_input("Ali zelis dodati nov izdelek na nakupovalni listek ? (da/ne): ")
    if dodaj == "da":
        izdelek = raw_input("Napisi izdelek, ki ga zelis dodati na listek: ")
        # preverja podvajanje elementov na nakupovalnem listku
        if izdelek in lisek:
            print("%s je ze na nakupovalnem listku" %(izdelek))
            izdelek = raw_input("Vpisi drug izdelek: ")
            lisek.append(izdelek)
        else:
            lisek.append(izdelek)
    elif dodaj == "ne":
        print("Dodajanje izdelkov na listek je koncno ")
        break
    else:
        print("Zelis dodati izdelek  vpisi da ali ne")

print("Tvoj listek vsebuje naseldnje izdelke:")
# izpse izdelke na sseznamu
for i in lisek:
    print(i)

