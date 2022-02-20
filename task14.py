def number(a):
    if a%2==0:
        print(f"Число '{a}' - чётное")
    else:
        print(f"Число '{a}' - не чётное")
n = int(input("Введите число:"))
number(n)
