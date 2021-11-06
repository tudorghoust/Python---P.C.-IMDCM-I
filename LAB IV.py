#EXERCITIUL 1

def inputs():
    x = int(input("X: "))
    if x<0:
        print("eroare numar ngativ")
    else:
        return x;

def functii(x):
    i = 2
    e = x
    while i < x+1:
        e += x/i
        i += 1
    print("E:",e)
    i = 2
    e = x
    for i in range(2,x+1):
        e += x/i
        i += 1
    print("E:", e)
    i = 1
    p = 1
    while i != x+1:
        p *= i
        i += 1
    print("P:", p)
    p = 1
    for i in range(1,x+1):
        p *= i
        i += 1
    print("P:", p)
    i = 1
    s = 0
    while i != x+1:
        s = s + (3*i-2)**2
        i += 1
    print("S:", s)
    s = 0
    for i in range(1, x + 1):
        s = s + (3*i-2)**2
        i += 1
    print("S:", s)

x = inputs()
functii(x)

#ex2

def inp():
    x, y = int(input("X: ")), int(input("Y: "))
    return x,  y;

def apr(x,y):
    cop = y
    c = 0
    ycf = 0
    if y > x:
        aux = y
        y = x
        x = aux
    cop1 = y
    while cop1:
        ycf += 1
        cop1 /= 10
    cop1 = y
    while x:
        ucx = x%10
        while ycf:
            ucy = y%10
            if ucy == ucx:
                c = 1
                break
            else:
                c = 0
            y = int(y/10)
            ycf -= 1
        y = cop
        x = int(x/10)
    if c:
        print("Cele doua numere sunt formate din aceleasi cifre")
    else:
        print("Cele doua numere nu sunt formate din aceleasi cifre")

x, y = inp()
apr(x, y)

#EX 3
def prdiv():
    x = int(input("X: "))
    k = 2
    mx = 0
    j = 0
    c = 0
    while x > 0:
        q = int(x/2)+1
        if x == 2:
            k = 2
        elif x == 1:
            k = 1
        else:
            for i in range(2,q):
                if x % i == 0:
                    k += 1
        if k > mx:
            mx = k
            j = 1
            c = x
        elif k == mx:
            j += 1
        x = int(input("X: "))
        k = 2
    print("Exista",j,"numere cu exact", mx, "divizori, iar unul dintre numere este", c)

prdiv()

#EX 4
def inp():
    x = int(input("X: "))
    return x;

def prt2(x):
    cop2 = x
    i = 1
    while x:
        for cop in range(x,1,-1):
            print(" ", end = ' ')
        for k in range(1, i+1):
            print(k, end = ' ')
        for j in range(cop2,x,-1):
            print(j-x, end=' ')
        print("")
        i = i + 1
        x = x - 1

def prt1(x):
    cop = x
    l = 0
    i = 1
    while x:
        for k in range(x,1,-1):
            print(" ", end = ' ')
        for j in range(cop-x+1,0,-1):
            print(j, end=' ')
        l += 1
        for i in range(i, l):
            print(i+1, end=' ')
        print(" ")
        x -= 1
        i = 1

def prt3(x):
    cop = x
    for i in range (0,cop,1):
        print(i+1, end = ':')
        x -= 1
        for k in range (0,cop-x,1):
            print(i+1, end ='')
            if(cop-x-1 != k):
                 print(end=',')
        print("")

def prt4(x):
    cop = x
    for i in range (1,cop+1,1):
        print(i, end = ':')
        x -= 1
        for k in range (1,i+1,1):
            if i % k == 0:
                print(k, end='')
                if i != k:
                     print(end =',')
        print("")

def prt5(x):
    cop = x
    for j in range(1,x*x+1):
        if j % 2 == 0:
            print(0, end = ' ')
        elif j % 2 == 1:
            print(1, end = ' ')
        if cop == j:
            print("")
            cop += x

def prt6(x):
    cop = x
    q = 1
    j = 1
    while q != x+1:
        if cop == j:
            print(j)
            q += 1
            j = q
            cop += 1
        else:
            print(j, end = ' ')
            j += 1

x = inp()
prt1(x)
print(" ")
prt2(x)
print(" ")
prt3(x)
print(" ")
prt4(x)
print(" ")
prt5(x)
print(" ")
prt6(x)


#EX 5
def tinm():
    for i in range(0,11):
        for j in range(1,11):
            print(j,"*",i,"=",i*j)

tinm()


#EX 6
def prs():
    x = int(input("X:"))
    mx = 0
    mn = 99999999
    s1 = 0
    s = 0
    k = 1
    for i in range(0,x):
        n = int(input("N:"))
        c = 1
        for j in range(2,n):
            if n % j == 0:
                c = 0
        if(n > mx and c):
            mx = n
        if(n < mn and c):
            mn = n
        cop = n
        if n > 9:
            ucf = n % 10
            n = int(n/10)
            while n:
                ucf1 = n % 10
                if(ucf < ucf1):
                    k = 0
                    s = 0
                    break
                else:
                    ucf = ucf1
                n = int(n/10)
            if k:
                s1 = s1+cop
            else:
                k = 1
        elif n < 10:
            s1 = s1+cop
    if (mn == 99999999 or mn == 0 or mx == 0):
        print("eroare")
    print("Cel mai mare nr prim:", mx,"Cel mai mic nr prim:", mn)
    print("Suma numarelor care au cifre in ordine crescatoare:",s1)

prs()


#EX7
def ascji():
    d = 0
    while d <= 255:
        print("%d = %c" % (d, chr(d)))
        d += 1

ascji()

#EX8
def parmin():
    mn = 99999999
    c = 1
    s = 0
    x = int(input("X:"))
    while x:
        if x % 2 == 0:
            s += x
        if mn > x:
            mn = x
            c = 1
        elif mn == x:
            c += 1
        x = int(input("X:"))
    print("Suma valorilor pare:",s,"Minimul este:",mn,"si apare de",c,"ori")

parmin()


def inp():
    x, y = int(input("X: ")), int(input("Y: "))
    return x,  y;

def apr(x,y):
    cop = y
    c = 0
    ycf = 0
    if y > x:
        aux = y
        y = x
        x = aux
    cop1 = y
    while cop1:
        ycf += 1
        cop1 /= 10
    cop1 = y
    while x:
        ucx = x%10
        while ycf:
            ucy = y%10
            if ucy == ucx:
                c = 1
                break
            else:
                c = 0
            y = int(y/10)
            ycf -= 1
        y = cop
        x = int(x/10)
    if c:
        print("Cele doua numere sunt formate din aceleasi cifre")
    else:
        print("Cele doua numere nu sunt formate din aceleasi cifre")

x, y = inp()
apr(x, y)
