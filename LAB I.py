#PROBLEMA I
def brad():
    print("    *\n   ***\n  *****\n *******\n   ***\n")
brad()

#PROBELMA II
def nr3():
    x,y,z = input("Introduceti 3 numere: ").split()
    print("Cele trei numere in ordine inversa introdusa sunt:", z, y, x)
nr3()

#PROBLEMA III
def medarit2():
    a, b = float(input("Introduceti:\nPrimul numar ")), float(input("Al doilea numar "))
    m = (a+b)/2
    print("Media aritmetica este:", float(m))
medarit2()

#PROBLEMA IV
def citire():
    a, b, c ,d = float(input("Introduceti:\nPrimul numar: ")), float(input("Al doilea numar: ")), float(input("Introduceti al treilea numar: ")), float(input("Introduceti al patrulea numar: "))
    return a, b, c, d;

def calc(a, b, c, d):
    M = (a+b+c)/3
    F = (a+3)/2+b
    E = (a+b)/2+(d*c)/3
    return M, F, E;

def afisare(M, F, E):
    print("M = ", M, "F = ", F, "E = ", E)

a, b, c, d = citire()
M, F, E = calc(a, b ,c ,d)
afisare(M, F, E)

#PROBLEMA V
def afis():
    print("Ma numesc \"ghilimea\" si nu arat asa \'.\nEu, adica \\, sunt un backslash.\n\tAcum am \'sarit\' un tab  ")
afis()

#PROBLEMA VI
def cal():
    x = float (input("Introduceti numar: "))
    print("Calculul numarului este: ", (x-1)/(x**2))
cal()

#PROBLEMA VII
import math

def convtip():
    x = float(input("Introduceti numar: "))
    x, i = math.modf(x)
    #x-int(x)
    print("Partea fractionara este: ", x)
convtip()

#PROBLEMA VIII
def exp():
    a, b = int(input("Introduceti:\nPrimul numar: ")), int(input("Al doilea numar: "))
    E = (a-b)/(a+b)
    print("Valoarea expresiei este: ", E)
exp()

#PROBLEMA IX
def citire():
    a, b, c = float(input("Introduceti:\nPrimul numar: ")), float(input("Al doilea numar: ")), float(input("Introduceti al treilea numar: "))
    return a, b, c;

def mij(a, b, c):
    m = a + b + c - max(a, b, c) - min(a, b, c)
    return int(m);

def afisare(m):
    print("Numarul mijlociu este = ", m)

a, b, c = citire()
m = mij(a, b ,c)
afisare(m)

#PROBLEMA X
def citire():
    a, b, c = float(input("Introduceti:\nPrimul numar: ")), float(input("Al doilea numar: ")), float(input("Introduceti al treilea numar: "))
    return a, b, c;

def smin(a, b, c):
    m = a + b + c - max(a, b, c)
    return int(m);

def afisare(m):
    print("Suma celor mai mici valori = ", m)

a, b, c = citire()
m = smin(a, b ,c)
afisare(m)
