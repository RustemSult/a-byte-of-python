# -*- coding: utf-8 -*- 

# для самопроверки после блока '/ ...code... /'
# удалите код, если он есть, и выполните задание повторно


x = 7
print('Значение x составляет', x)

# Создайте функцию newFunc
# / ...code... /
def newFunc():
    res = x * 10
    print('x = {}, res = {}'.format(x, res))

newFunc() # проверка функции

# Создайте функцию newFunc2 с 3 параметрами
# / ...code... /
def newFunc2(a, b, c):
    x = a * b * c
    print('x = {} * {} * {} = {}'.format(a, b, c, x))

newFunc2(x, 3, 5)
print('Значение x составляет', x)

# Создайте функцию newFunc3 с изменением глобальных значений x
# / ...code... /
def newFunc3(a, b, c):
    global x
    x = a * b * c
    print('x = {} * {} * {} = {}'.format(a, b, c, x))

newFunc3(x, 10, 10)
print('Значение x составляет', x)

# Создайте функцию newFunc4 с внутренней переменной x
# и c дополнительной функцией внутри, для изменения глобальных значений x
# / ...code... /
def newFunc4(a, b, c):
    x = a / b / c
    print('x = {} / {} / {} = {}'.format(a, b, c, x))

    def inner():
        global x
        x /= 2
        print('Update x =', x)    
    inner()

x = 15
print('Значение x составляет', x)

newFunc4(x, 2, 3)
print('Значение x составляет', x)

# Создайте функцию newFunc5 с внутренней переменной x
# и c дополнительной функцией внутри, для обработки только локальных значений x
# / ...code... /
def newFunc5(a, b, c):
    x = a / b / c
    print('x = {} / {} / {} = {}'.format(a, b, c, x))

    def inner():
        nonlocal x
        x /= 2
        print('Update x =', x)    
    inner()

x = 15
print('Значение x составляет', x)

newFunc5(x, 2, 3)
print('Значение x составляет', x)

# Создайте функцию newFunc6 с 1 ключевым и 2 аргументами по умолчанию
# / ...code... /
def newFunc6(a, b = 1, c = 1):
    x = a / b / c
    print('x = {} / {} / {} = {}'.format(a, b, c, x))

newFunc6(7)
newFunc6(27, 7, 3)

# Создайте функцию totalFunc с переменным число параметров
# / ...code... /
def totalFunc(a, *number, **namevar):
    s = ''
    d = 1
    for i in number:
        d /= i
        s += ' / %s' % str(i)
    for i in namevar:
        d /= namevar[i]
        s += ' / %s' % str(namevar[i])    
    print('y = {}{} = {}'.format(a, s, a*d))

totalFunc(16, 2)
totalFunc(16, 2, 3, 4)
totalFunc(265, 62, 23, 12, 40, 2, 3, 4, 5)
totalFunc(8, 1, 7, 3, var1=1.5, var2=0.56)
totalFunc(8, var1=1.5, var2=0.56)
totalFunc(x)

# Создайте функцию totalFunc2 с только ключевыми параметрами
# / ...code... /
def exper(x, step):
    '''exper(x) - пробная функция расчета

    Если введено не целое число, то будет округление до целого. Строковые типы не обрабатываются.
    '''
    x = int(x)
    step = int(step)
    res = x / 1
    for i in range(x - 1, 0, -step):
        res /= i
    return res

exper(1)
print(exper(1, step=1))

print(exper(3, step=1))
print(exper(4, step=1))
totalFunc(4, 3, 2, 1)

print(exper(10, step=1))
totalFunc(10, 9, 8, 7, 6, 5, 4, 3, 2, 1)

print(exper(100, step=1))

print(exper(59, step=1))
print(exper(100, step=2))
print(exper(100, step=2.5))

# Создайте функцию summa оператором «return» c документацией DocStrings
# / ...code... /
def factorial(x):
    '''factorial(x) - функция расчета факториала числа

    Если введено не целое число, то будет округление до целого. Строковые типы не обрабатываются.
    '''
    x = int(x)
    res = 1
    for i in range(1, x + 1):
        res *= i
    return res

print(factorial(3))
print(factorial(50))
print(factorial(51.1))
print(factorial(x))
print(factorial(0))

print(factorial.__doc__)


print("\n--- End ---")