print("Число Фибоначчи")
n= int(input("Введите число: "))
a = b = 1
c = a + b
while c<=n:
    a = b + c
    a, b, c = b, c, a
if b == n:
    print("Принадлежит")
else:
    print("Не принадлежит")
