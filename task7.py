def num(a, b, c):
    if b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    else:
        return a
k = int(input("First num: "))
l = int(input("Second num: "))
j = int(input("Third num: "))
print(num(k,l,j))
