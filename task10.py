from calendar import c


def op(a,b,c):
    if c == "*":
        print(a*b)
    elif c == "/":
        print(a/b)
    elif c == "+":
        print(a+b)
    elif c == "-":
        print(a-b)
    else:
        print("Unknown operation")
k = int(input("First num: "))
j = int(input("Second num: "))
l = input("Enter operation please (*,/,+,-)")
op(k,j,l)