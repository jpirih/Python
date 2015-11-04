# ali je stevilo sodo ali liho
# user inputs number and program tells him if the number is odd or even
# uporabniku tudi pove ce je stevilo deljivo s 4 in pove ce sta obe stevli med sabo
# deljivi brez ostanka

num = float(raw_input("Please insert number - Prosim vesi stevilo: "))
check = float(raw_input("Please enter second number - Prosim vnesi drugo stevilo: "))
if num % 2 == 0 and num % 4 != 0:
    print("stevilo %d je sodo (The number is even)" %(num))
elif num %2 == 0 and num % 4 == 0:
    print("stevilo %d je veckratnik stevil 4 (the number is multiple of 4)" %(num))
    print("stevilo %d je sodo (The number is even)" %(num))
else:
    print("stevilo %d je liho (The number is odd)" %(num))

if num % check == 0:
    ostanek = num % check
    print("stevilo %d je deljivo s stevilom %d brez ostanka (The two numbers are devided evenly)"%(num, check))
else:
    ostanek = num % check
    print("pri deljenju stevil %d in %d znasa ostanek %d" %(num, check, ostanek))