# -*- coding: utf-8 -*- 


print("--- Функции ---\n")


# Пример: (сохраните как function1.py )
# Создаем функцию sayHello
def sayHello():
    print('Привет, Мир!') # блок, принадлежащий функции
# Конец функции

sayHello() # вызов функции


## Параметры функций

# Пример: (сохраните как func_param.py)
def printMax(a, b):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'равно', b)
    else:
        print(b, 'максимально')

printMax(3, 4) # прямая передача значений

x = 5
y = 7
printMax(x, y) # передача переменных в качестве аргументов


## Локальные переменные

# Пример: (сохраните как func_local.py)
x = 50

def func_loc(x):
    print('x равен', x)
    x = 2
    print('Замена локального x на', x)

func_loc(x)
print('x по прежнему', x)


## Зарезервированное слово «global»

# Пример: (сохраните как func_global.py)
x = 50

def func_glob():
    global x

    print('x равно', x)
    x = 2
    print('Заменяем глобальное значение x на', x)

func_glob()
print('Значение x составляет', x)


## Зарезервированное слово «nonlocal»

# Есть ещё один тип области видимости, называемый «нелокальной» (nonlocal)
# областью видимости, который представляет собой нечто среднее между первыми 
# двумя. Нелокальные области видимости встречаются, когда вы определяете 
# функции внутри функций.

# Filename: func_nonlocal.py
def func_outer():
    x = 2
    print('x локально равно', x)

    def func_inner():
        nonlocal x # nonlocal | global
        x = 5
    
    func_inner()
    print('Локальное x сменилось на', x)

    #func_glob()
    #print('Локальное значение x составляет', x)

x = 70
print('Значение x составляет', x)

func_outer()
print('Значение x составляет', x)

# Попробуйте заменить «nonlocal x» на «global x», а затем удалить это
# зарезервированное слово, и пронаблюдайте за разницей между этими двумя
# случаями.

# Попробуйте вариант с функцией func_glob() внутри func_outer().


## Значения аргументов по умолчанию

# Обратите внимание, что значение по умолчанию должно быть константой. 
# Или точнее говоря, оно должно быть неизменным(«immutable»).

# Пример: (сохраните как func_default.py)
def say(message, times = 1):
    print(message * times)

say('Привет')
say('Мир', 5)
say('Мир ', 5)

# Важно: Значениями по умолчанию могут быть снабжены только параметры, 
# находящиеся в конце списка параметров. Таким образом, в списке параметров 
# функции параметр со значением по умолчанию не может предшествовать 
# параметру без значения по умолчанию. Это связано с тем, что значения
# присваиваются параметрам в соответствии с их положением. 
# 
# Например, def func(a, b=5) допустимо, 
# а def func(a=5, b) - не допустимо.


## Ключевые аргументы

# Пример: (сохраните как func_key.py)
def func(a, b=5, c=10):
    print('a равно', a, ', b равно', b, ', а c равно', c)

func(3, 7)
func(25, c=24)
func(c=50, a=100)
func(c=50, a=100, b=7)


## Переменное число параметров

# Иногда бывает нужно определить функцию, способную принимать любое 
# число параметров. Этого можно достичь при помощи звёздочек 
# (сохраните как total.py):
def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count

print(total(10, 1))
print(total(10, 1, 2, 3))
print(total(10, 1, 2, 3, vegetables=50, fruits=100))


## Только ключевые параметры

# Если некоторые ключевые параметры должны быть доступны только по ключу, 
# а не как позиционные аргументы, их можно объявить после параметра со 
# звёздочкой (сохраните как keyword_only.py):
def total2(initial=5, *numbers, extra_number):
    count = initial
    for number in numbers:
        count += number
    count += extra_number
    print(count)

total2(10, 1, 2, 3, extra_number=50)
# total2(10, 1, 2, 3)
# Вызовет ошибку, поскольку мы не указали значение
# аргумента по умолчанию для 'extra_number'.

# Если вам нужны аргументы, передаваемые только по ключу, но не нужен
# параметр со звёздочкой, то можно просто указать одну звёздочку без 
# указания имени: def total3(initial=5, *, extra_number).


## Оператор «return»

# Пример: (сохраните как func_return.py)
#!/usr/bin/python
# Filename: func_return.py
def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'Числа равны.'
    else:
        return y

print(maximum(2, 3))

# Обратите внимание, что оператор return без указания возвращаемого значения
# эквивалентен выражению return None . None – это специальный тип данных 
# в Python, обозначающий ничего. К примеру, если значение переменной установлено
# в None , это означает, что ей не присвоено никакого значения.

def someFunction():
    pass

# Оператор pass используется в Python для обозначения пустого блока команд.

print(someFunction())


## Строки документации DocStrings

# Пример: (сохраните как func_doc.py)
def printMaximum(x, y):
    '''Выводит максимальное из двух чисел.

    Оба значения должны быть целыми числами.'''
    x = int(x) # конвертируем в целые, если возможно
    y = int(y)
    
    if x > y:
        print(x, 'наибольшее')
    else:
        print(y, 'наибольшее')

printMaximum(3, 5)
print(printMaximum.__doc__)
# Поразительно, но строку документации можно получить,
# например, из функции, даже во время выполнения программы!

# Строка в первой логической строке функции является строкой документации
# для этой функции. Обратите внимание на то, что строки документации 
# применимы также к модулям и классам, о которых мы узнаем в соответствующих
# главах.
# Строки документации принято записывать в форме многострочной строки,
# где первая строка начинается с заглавной буквы и заканчивается точкой. 
# Вторая строка оставляется пустой, а подробное описание начинается с третьей.
# Вам настоятельно рекомендуется следовать такому формату для всех строк
# документации всех ваших нетривиальных функций.
# Доступ к строке документации функции printMax можно получить с помощью
# атрибута этой функции (т.е. имени, принадлежащего ей) __doc__ 
# (обратите внимание на двойное подчёркивание). Просто помните, что Python 
# представляет всё в виде объектов, включая функции.

# help(printMaximum)
# Не забудьте нажать клавишу q для выхода из справки ( help ).


## Аннотации

# Этот функционал отводится посторонним библиотекам, подробнее см. ссылку
# https://www.python.org/dev/peps/pep-3107/


print("\n--- End ---")
