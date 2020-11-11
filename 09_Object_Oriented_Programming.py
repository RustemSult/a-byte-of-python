# -*- coding: utf-8 -*- 


print("--- Объектно-ориентированное программирование ---\n")

# Два основных аспекта объектно-ориентированного программирования – классы 
# и объекты. Класс создаёт новый тип, а объекты являются экземплярами класса.

# Переменные, принадлежащие объекту или классу, называют полями. Объекты могут
# также обладать функционалом, т.е. иметь функции, принадлежащие классу. 
# Такие функции принято называть методами класса.

# Всё вместе (поля и методы) принято называть атрибутами класса.

# Поля бывают двух типов: они могут принадлежать каждому отдельному экземпляру
# объекта класса или всему классу. Они называются переменными экземпляра и
# переменными класса соответственно.


## self

# self в Python эквивалентно указателю this в C++ и ссылке this в Java и C#.

# Предположим, у нас есть класс с именем MyClass и экземпляр этого класса с именем myobject.
# При вызове метода этого объекта, например, “ myobject.method(arg1, arg2) ”, 
# Python автоматически превращает это в “ MyClass.method(myobject, arg1, arg2) ” – 
# в этом и состоит смысл self.

# Это также означает, что если какой-либо метод не принимает аргументов, у него всё 
# равно будет один аргумент – self .


## Классы

# Простейший класс показан в следующем примере (сохраните как simplestclass.py).
class Person:
    pass # Пустой блок

p = Person()
print(p)

# $ python3 simplestclass.py


## Методы объектов

# А теперь давайте рассмотрим пример (сохраните как method.py).
class Person:
    def sayHi(self):
        print('Привет! Как дела?')

p = Person()
p.sayHi()

# Этот короткий пример можно также записать как Person().sayHi()

# $ python3 method.py


## Метод __init__

# Пример: (сохраните как class_init.py )
class Person:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print('Привет! Меня зовут', self.name)

p = Person('Swaroop')
p.sayHi()

# Этот короткий пример можно также записать как Person('Swaroop').sayHi()

# $ python3 class_init.py


## Переменные класса и объекта

# Данные, т.е. поля, являются не чем иным, как обычными переменными,
# заключёнными в пространствах имён классов и объектов. Это означает,
# что их имена действительны только в контексте этих классов или объектов.
# Отсюда и название «пространство имён».

# (сохраните как objvar.py):
class Robot:
    '''Представляет робота с именем.'''
    # Переменная класса, содержащая количество роботов
    population = 0
    
    def __init__(self, name):
        '''Инициализация данных.'''
        self.name = name
        print('(Инициализация {0})'.format(self.name))

        # При создании этой личности, робот добавляется
        # к переменной 'population'
        Robot.population += 1
    
    def __del__(self):
        '''Я умираю.'''
        print('{0} уничтожается!'.format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print('{0} был последним.'.format(self.name))
        else:
            print('Осталось {0:d} работающих роботов.'.format(Robot.population))
    
    def sayHi(self):
        '''Приветствие робота.
        
        Да, они это могут.'''
        print('Приветствую! Мои хозяева называют меня {0}.'.format(self.name))
    
    def howMany():
        '''Выводит численность роботов.'''
        print('У нас {0:d} роботов.'.format(Robot.population))

    howMany = staticmethod(howMany)

droid1 = Robot('R2-D2')
droid1.sayHi()
Robot.howMany()

droid2 = Robot('C-3PO')
droid2.sayHi()
Robot.howMany()

print("\nЗдесь роботы могут проделать какую-то работу.\n")

print("Роботы закончили свою работу. Давайте уничтожим их.")
del droid1
del droid2

Robot.howMany()

# ... Мы могли достичь того же самого, используя декораторы:
@staticmethod
def howMany():
    '''Выводит численность роботов.'''
    print('У нас {0:d} роботов.'.format(Robot.population))


## Наследование

# Легче всего представить себе наследование в виде отношения
# между классами как тип и подтип.

# ... Когда подтип может быть подставлен в любом месте, где ожидается
# родительский тип, т.е. объект считается экземпляром родительского класса,
# это называется полиморфизмом.

# Заметьте также, что код родительского класса используется многократно, и нет необхо-
# димости копировать его во всех классы, как пришлось бы в случае использования неза-
# висимых классов.

# Класс SchoolMember в этой ситуации называют базовым классом или надклассом 3. Классы
# Teacher и Student называют производными классами или подклассами 4.

# Рассмотрим теперь этот пример в виде программы (сохраните как inherit.py):

class SchoolMember:
    '''Представляет любого человека в школе.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Создан SchoolMember: {0})'.format(self.name))
    
    def tell(self):
        '''Вывести информацию.'''
        print('Имя:"{0}" Возраст:"{1}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
    '''Представляет преподавателя.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        # !!! Python не вызывает конструктор базового класса автоматически -
        # его необходимо вызывать самостоятельно в явном виде.
        self.salary = salary
        print('(Создан Teacher: {0})'.format(self.name))
    
    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата: "{0:d}"'.format(self.salary))

class Student(SchoolMember):
    '''Представляет студента.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Создан Student: {0})'.format(self.name))
    
    def tell(self):
        SchoolMember.tell(self)
        print('Оценки: "{0:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

print() # печатает пустую строку

members = [t, s]
for member in members:
    member.tell() # работает как для преподавателя, так и для студента

# Вывод:
# $ python3 inherit.py

# Замечание по терминологии: если при наследовании перечислено более
# одного класса, это называется множественным наследованием.


## Метаклассы

#!/usr/bin/env python
# Filename: inherit_abc.py

from abc import *

class SchoolMember(metaclass=ABCMeta):
    '''Представляет любого человека в школе.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Создан SchoolMember: {0})'.format(self.name))

    @abstractmethod
    def tell(self):
        '''Вывести информацию.'''
        print('Имя:"{0}" Возраст:"{1}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
    '''Представляет преподавателя.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Создан Teacher: {0})'.format(self.name))
    
    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата: "{0:d}"'.format(self.salary))

class Student(SchoolMember):
    '''Представляет студента.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Создан Student: {0})'.format(self.name))
    
    def tell(self):
        SchoolMember.tell(self)
        print('Оценки: "{0:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

#m = SchoolMember('abc', 10)
# Это приведёт к ошибке: "TypeError: Can't instantiate abstract class
# SchoolMember with abstract methods tell"

print() # печатает пустую строку

members = [t, s]
for member in members:
    member.tell() # работает как для преподавателя, так и для студента

# Вывод:
# $ python3 inherit.py


print("\n--- End ---")
