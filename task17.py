import math
def trik(a,b,c):
    p = (a+b+c)
    s = round(math.sqrt (p*(p-a)*(p-b)*(p-c)))
    print(s)
def trik_check(a,b,c):
    if a+ b > c and a + c > b and b + c > a:
        return True
    else:
        return False
def kryg(r):
    so = math.pi * r**2
    print(so)
def prymokut(a,b):
    sp = a * b
    print(sp)
def figura(figur):
    if figur == "kryg":
        q = int(input("Напиши радиус: "))
        kryg(q)
    elif figur == "trik":
        a = int(input("сторона1: "))
        b = int(input("сторона2: "))
        c = int(input("сторона3: "))
        trik(a,b,c)
        if trik_check(a,b,c):
            trik(a,b,c)
        else:
            print("Такой треугольник не существует")
    elif figur == "prymokut":
        n = int(input("Введите 1 сторону: "))
        z = int(input("Введите 2 сторону: "))
        prymokut(n,z)
figura(input("Введите фигуру (trik,kryg,prymokut): "))
