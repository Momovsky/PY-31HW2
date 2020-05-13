def polish_notation(a, b, c):
    assert a in ['+', '-', '*', '/'], "Вы ввели неверную операцию"
    try:
        int(b)+int(c)
    except ValueError:
        return "Вы ввели строку вместо числа"
    else:
         if a == '+':
             return int(b) + int(c)
         elif a == '-':
             return int(b) - int(c)
         elif a == '*':
             return int(b) * int(c)
         elif a == '/':
             try:
                 int(b) / int(c)
             except ZeroDivisionError:
                 return "Вы попытались разделить на ноль"
             else:
                 return int(b) / int(c)

polish_statement = [i for i in input('Введите выражение в Польской нотации: ').split()]
try:
    polish_notation(*polish_statement)
except TypeError:
    print("Вы ввели недопустимое количество аргументов. Введите оператор и два операнда через пробел")
else:
    print(polish_notation(*polish_statement))