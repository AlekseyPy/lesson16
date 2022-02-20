def trik(a,b,c):
    if a+ b > c and a + c > b and b + c > a:
        print("Это треугольник")
    else:
        print("Это не треугольник")
k = int(input("A = "))
l = int(input("B = "))
f = int(input("C = "))
trik(k,l,f)