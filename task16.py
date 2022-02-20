def factorial(a):
    a=1
    for i in range(2, a+1):
        a*=i
b = int(input("Enter number: "))
print(b)

#или же есть другой способ

import math
a = int(input("n = "))
print(f"Факториал числа {a} - {math.factorial(a)}")