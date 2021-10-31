#PROBLEMA 1
def citire():
    x, y = int(input("X: ")) ,int(input("Y: "))
    return x, y;

def funcat(x, y):
    if (x < 0):
        print(x+y)
    elif (x >= 0):
        print(x*y)

x, y = citire()
funcat(x, y)

#PROBLEMA 2
def citire():
    x, y, z = int(input("X: ")), int(input("Y: ")), int(input("Z: "))
    return x, y, z;

def mima(x ,y ,z):
    if (x > y):
        min = y
        max = x
    else:
        min = x
        max = y
    if (z > max):
        max = z
    if (z < min):
        min = z
    print("Max: ", max, "Min: ", min)

x, y ,z = citire()
mima(x, y, z)

#PROBLEMA 3
def citire():
    x, y, z = int(input("X: ")), int(input("Y: ")), int(input("Z: "))
    return x, y, z;

def verifpoz(x, y, z):
    if (x > 0 and y > 0 and z > 0 ):
        return 1;
    else:
        return 0;

def afisareordcresc(x ,y ,z):
    if (verifpoz(x ,y ,z)):
        if (x > y):
            min = y
            max = x
        else:
            min = x
            max = y
        if (z > max):
            max = z
        if (z < min):
            min = z
        print("Numere ord cresc sunt: ", min, x+y+z-min-max, max)
    else:
        print("WE HAVE A PROBLEM")

x, y ,z = citire()
verifpoz(x, y, z)
afisareordcresc(x, y, z)

#PROBLEMA IV
def citire():
    x, y, z = int(input("X: ")), int(input("Y: ")), int(input("Z: "))
    return x, y, z;

def verifpar(x, y, z):
    if (x % 2 == 0):
        print(x)
    if(y % 2 == 0):
        print(y)
    if(z % 2 == 0):
        print(z)

x, y ,z = citire()
verifpar(x, y, z)

#PROBLEMA V
def citire():
    x = int(input("X: "))
    return x;

def ucput2(x):
    if x == 0:
        print (1)
    elif x % 4 == 1:
        print (2)
    elif x % 4 == 2:
        print (4)
    elif x % 4 == 3:
        print (8)
    else:
        print(6)

x = citire()
ucput2(x)

#PROBLEMA VI
def citire():
    a, b = int(input("A: ")), int(input("B: "))
    return a, b;

def ecgrd1(a, b):
    if b > 0:
        c = -b
    else:
        c = abs(b)
    c /= a
    print(c)

a, b = citire()
ecgrd1(a, b)

#PROBLEMA VII
def citire():
    a = input("Introduceti un caracter: ")
    return a

def veriflowupp(a):
    if a in "abcdefghijklmnopqrstuvwxyz":
        print("Acest caracter este lowercase")
    elif a in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print("Acest caracter este uppercase")
    else:
        print("Acest caracter nu este lowercase si nici uppercase")

a = citire()
veriflowupp(a)

#PROBLEMA VII
def citire():
    a = int(input("A: "))
    return a;

def div5(a):
    if a % 5 == 0:
        print("Numarul este divizibil cu 5")
    else:
        print("Numarul nu este divizibil cu 5")

a = citire()
div5(a)

#PROBLEMA IX
def citire():
    a = int(input("A: "))
    return a;
def oprcond(a):
    e = a if a < 7 else 7 if (a if a < 7 else 7) > (a - 7 if a > 7 else 7-a) else (a-7 if a > 7 else 7 - a)
    print(e)
a = citire()
oprcond(a)

#PROBLEMA X
def citire():
    a = int(input("A: "))
    return a;
def sapt(a):
    if a == 1:
        print("Luni")
    if a == 2:
        print("Marti")
    if a == 3:
        print("Miercuri")
    if a == 4:
        print("Joi")
    if a == 5:
        print("Vineri")
    if a == 6:
        print("Sambata")
    if a == 7:
        print("Vineri")

a = citire()
sapt(a)