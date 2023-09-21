import math

def okr(num, sign, op=0):
    num = (str(num)+"0").split(".")
    print(num[1][sign])
    if num[1][sign] == "0" or op == 1:
        answer = num[0] + "."
        for i in range(sign):
            answer += num[1][i]
            print(answer)
        return answer
    else:
        answer = num[0] + "."
        for i in range(sign):
            if i < sign - 1:
                answer += num[1][i]
                print(answer)
            else:
                answer += str(int(num[1][i])+1)
                print(answer) 
        return answer
        

do = 0
while do != "":
    print("Для сложения введите +")
    print("Для вычитания введите -")
    print("Для умножения введите *")
    print("Для деления введите /")
    print("Для возвдения числа в степень введите **")
    print("Для нахождения логарифма введите log")
    print("Для округления в большую сторону до N знака после запятой введите okr+")
    print("Для округления в меньшую сторону до N знака после запятой  введите okr-\n")
    operation = ["+", "-", "*", "/", "**", "log", "okr+", "okr-", ""]
    while do not in operation:
        do = input("Действие: ")
    if do == "":
        break
    number1 = float(input("Введите первый элемент: "))
    number2 = float(input("Введите второй элемент: "))

    if do == operation[0]:
        print("Cумма", number1 + number2)
    elif do == operation[1]:
        print("Разница", number1 - number2)
    elif do == operation[2]:
        print("Произведение", number1 * number2)
    elif do == operation[3]:
        print("Частное", number1 + number2)
    elif do == operation[4]:
        print("{0}^{1} = {2}".format(number1, number2, number1 ** number2))
    elif do == operation[5]:
        print("log{0}({1}) = {2}".format(number1, number2, math.log(number2, number1)))
    elif do == operation[6]:
        print(okr(str(number1), int(number2), 0))
    else:
        print(okr(str(number1), int(number2), 1))

    do = 0


    

