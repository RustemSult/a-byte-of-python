# -*- coding: utf-8 -*- 
# $ - При таком символе нужно переключиться в командную строку (CLI)


print("--- Модули ---\n")


## Модули

# Пример: (сохраните как using_sys.py )
import sys

print('Аргументы командной строки:')
for i in sys.argv:
    print(i)

print('\n\nПеременная PYTHONPATH содержит', sys.path, '\n')

# Вывод (Enter in terminal):
#$ python3 using_sys.py we are arguments

# Так что в приведённом примере 'using_sys.py'
# будет элементом sys.argv[0] , 'we' – sys.argv[1] , 'are' – sys.argv[2] , а
# 'arguments' – sys.argv[3].
# sys.path содержит список имён каталогов, откуда импортируются модули.
# Заметьте, что первая строка в sys.path пуста; эта пустая строка показывает,
# что текущая директория также является частью sys.path.
# Помните, что текущий каталог – это каталог, в котором была запущена про-
# грамма. Выполните import os; print(os.getcwd()) , чтобы узнать текущий
# каталог программы.

import os; print(os.getcwd())


## Файлы байткода .pyc

# Это байт-компилированные файлы (или байткод)

# Такой файл .pyc полезен при импорте модуля в следующий раз в другую 
# программу - это произойдёт намного быстрее, поскольку значительная 
# часть обработки, требуемой при импорте модуля, будет уже проделана. 
# Этот байткод также является платформо-независимым.


## Оператор from ... import ...

# Чтобы импортировать переменную argv прямо в программу и не писать 
# всякий раз sys. при обращении к ней, можно воспользоваться выражением
# “from sys import argv ”.
# Для импорта всех имён, использующихся в модуле sys , можно выполнить 
# команду “from sys import * ”. Это работает для любых модулей.

# !!! Cледует избегать использования “from ... * " и использовать
# вместо этого оператор import

# Пример:

from math import *
n = int(input("Введите диапазон:- "))

p = [2, 3]
count = 2
a = 5
while (count < n):
    b=0
    for i in range(2,a):
        if ( i <= sqrt(a)):
            if (a % i == 0):
                print("a neprost", a)
                b = 1
            else:
                pass

    if (b != 1):
        print("a prost", a)
        p = p + [a]
    count = count + 1
    a = a + 2
print(p)
print(a)


## Имя модуля – __name__

# Пример: (сохраните как using_name.py )

if __name__ == '__main__':
    print('Эта программа запущена сама по себе.')
else:
    print('Меня импортировали в другой модуль.')

# Вывод:
#$ python3 using_name.py
# Эта программа запущена сама по себе.
#$ python3
# >>> import using_name
# Меня импортировали в другой модуль.
# >>>

exit()

#$ cp prog/using_name.py using_name.py
#$ python3 using_name.py
# Помните, что модуль должен находиться либо в том же каталоге, что и программа,
# в которую мы импортируем его, либо в одном из каталогов, указанных в sys.path .

#$ python3
import using_name


## Создание собственных модулей

# Пример: (сохраните как mymodule.py )

def sayhi():
    print('Привет! Это говорит мой модуль.')

__version__ = '0.1'

# Конец модуля mymodule.py

#$ cp prog/mymodule.py mymodule.py
#$ python3
import mymodule
mymodule.sayhi()
print ('Версия', mymodule.__version__)
print ('Имя', mymodule.__name__)
#exit()

#$ cp prog/mymodule_demo.py mymodule_demo.py
#$ python3 mymodule_demo.py

# Вот версия, с синтаксисом from..import (сохраните как mymodule_demo2.py ):

from mymodule import sayhi, __version__

sayhi()
print('Версия', __version__)

#$ cp prog/mymodule_demo2.py mymodule_demo2.py
#$ python3 mymodule_demo2.py

#$ python3
import mymodule_demo2
print ('Версия', mymodule_demo2.__version__)
print ('Имя', mymodule_demo2.__name__)

# Вы могли бы также использовать:
from mymodule import *
# Это импортирует все публичные имена, такие как sayhi , но не импортирует __version__ ,
# потому что оно начинается с двойного подчёркивания


## Функция dir

# Пример:
#$ python3
import sys # получим список атрибутов модуля 'sys'
dir(sys)

import mymodule
import mymodule_demo
import mymodule_demo2
dir(mymodule)
dir(mymodule_demo)
dir(mymodule_demo2)

dir() # получим список атрибутов текущего модуля

a = 5 # создадим новую переменную 'a'
dir()

del a # удалим имя 'a'
dir()

# Обратите внимание, что функция dir() работает для любого объекта. Напри-
# мер, выполните “ dir('print') ”, чтобы увидеть атрибуты функции print , или
# “ dir(str) ”, чтобы увидеть атрибуты класса str .

dir(str)        # класс
dir('print')    # функция


## Пакеты

# Пакеты - это просто каталоги с модулями и специальным файлом __init__.py , 
# который показывает Python, что этот каталог особый, так как содержит модули Python.
# Они как правило расположены в sys.path.


print("\n--- End ---")
