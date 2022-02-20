def num(a, b):
    if a>b:
        return a
    elif a==b:
        return "equal"
    else:
        return b
c = int(input("First number: "))
e = int(input("Second number: "))
print(num(c, e))