# -*- coding: utf-8 -*- 


print("--- Структуры данных ---\n")


## Список

# Пример: (сохраните как using_list.py)

# Это мой список покупок
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']

print('Я должен сделать', len(shoplist), 'покупок.')

print('Покупки:', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\nТакже нужно купить риса.')
shoplist.append('рис')
print('Теперь мой список покупок таков:', shoplist)

print('Отсортирую-ка я свой список')
shoplist.sort()
print('Отсортированный список покупок выглядит так:', shoplist)

print('Первое, что мне нужно купить, это', shoplist[0])
olditem = shoplist[0]

del shoplist[0]
print('Я купил', olditem)
print('Теперь мой список покупок:', shoplist)

# $ cp prog/using_list.py using_list.py
# $ python3 using_list.py

# python3
help(list)


## Кортеж

# Пример: (сохраните как using_tuple.py)

zoo = ('питон', 'слон', 'пингвин') # помните, что скобки не обязательны
print('Количество животных в зоопарке -', len(zoo))

new_zoo = 'обезьяна', 'верблюд', zoo
print('Количество клеток в зоопарке -', len(new_zoo))
print('Все животные в новом зоопарке:', new_zoo)
print('Животные, привезённые из старого зоопарка:', new_zoo[2])
print('Последнее животное, привезённое из старого зоопарка -', new_zoo[2][2])
print('Количество животных в новом зоопарке -', len(new_zoo)-1+len(new_zoo[2]))

# $ cp prog/using_tuple.py using_tuple.py
# $ python3 using_tuple.py

# python3

# Помните что например,
print(1,2,3)
# ”и“ 
print( (1,2,3) )
# делают разные вещи: первое выражение выводит три числа, 
# тогда как второе – кортеж, содержащий эти три числа.

# Про кортеж, содержащий 0 или 1 элемент:

# Пустой кортеж создаётся при помощи пустой пары скобок – “myempty = ()”. 
# Однако, с кортежем из одного элемента не всё так просто. Его нужно указывать 
# при помощи за пятой после первого (и единственного) элемента, 
# чтобы Python мог отличить кортеж от скобок, окружающих объект в выражении. 
# 
# Таким образом, чтобы получить кортеж, содержащий элемент 2 , 
# вам потребуется указать “ singleton = (2,) ”.

singleton = (2,)
print(singleton)
type(singleton)

help(tuple)


## Словарь

# Пример: (сохраните как using_dict.py)

# 'ab' - сокращение от 'a'ddress'b'ook
ab = {
    'Swaroop'   : 'swaroop@swaroopch.com',
    'Larry'     : 'larry@wall.org',
    'Matsumoto' : 'matz@ruby-lang.org',
    'Spammer'   : 'spammer@hotmail.com'
}

print("Адрес Swaroop'а:", ab['Swaroop'])

# Удаление пары ключ-значение
del ab['Spammer']

print('\nВ адресной книге {0} контактов\n'.format(len(ab)))

for name, address in ab.items():
    print('Контакт {0} с адресом {1}'.format(name, address))

# Добавление пары ключ-значение
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nАдрес Guido:", ab['Guido'])

# Вывод:
# $ cp prog/using_dict.py using_dict.py
# python3 using_dict.py

# python3
help(dict)


## Последовательности

# Пример: (сохраните как seq.py)

shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
name = 'swaroop'

# Операция индексирования
print('Элемент 0 -', shoplist[0])
print('Элемент 1 -', shoplist[1])
print('Элемент 2 -', shoplist[2])
print('Элемент 3 -', shoplist[3])
print('Элемент -1 -', shoplist[-1])
print('Элемент -2 -', shoplist[-2])
print('Символ 0 -', name[0])

# Вырезка из списка
print('Элементы с 1 по 3:', shoplist[1:3])
print('Элементы с 2 до конца:', shoplist[2:])
print('Элементы с 1 по -1:', shoplist[1:-1])
print('Элементы от начала до конца:', shoplist[:])

# Вырезка из строки
print('Символы с 1 по 3:', name[1:3])
print('Символы с 2 до конца:', name[2:])
print('Символы с 1 до -1:', name[1:-1])
print('Символы от начала до конца:', name[:])

# Вывод:
# $ cp prog/seq.py seq.py
# $ python3 seq.py

# python3
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
shoplist[::1]
shoplist[::2]
shoplist[::3]
shoplist[::-1]


## Множество

bri = set(['Бразилия', 'Россия', 'Индия'])
'Индия' in bri
'США' in bri

bric = bri.copy()
bric.add('Китай')
bric.issuperset(bri)

bri.remove('Россия')

bri & bric # OR bri.intersection(bric)

# python3
help(set)


## Ссылки

# Пример: (сохраните как reference.py)

print('Простое присваивание')
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
mylist = shoplist # mylist - лишь ещё одно имя, указывающее на тот же объект!

del shoplist[0] # Я сделал первую покупку, поэтому удаляю её из списка

print('shoplist:', shoplist)
print('mylist:', mylist)
# Обратите внимание, что и shoplist, и mylist выводят один и тот же список
# без пункта "яблоко", подтверждая тем самым, что они указывают на один объект.

print('Копирование при помощи полной вырезки')
mylist = shoplist[:] # создаём копию путём полной вырезки
del mylist[0] # удаляем первый элемент

print('shoplist:', shoplist)
print('mylist:', mylist)
# Обратите внимание, что теперь списки разные

# Вывод:
# $ cp prog/reference.py reference.py
# $ python3 reference.py


## Ещё о строках

# Пример: (сохраните как str_methods.py)

name = 'Swaroop' # Это объект строки
if name.startswith('Swa'):
    print('Да, строка начинается на "Swa"')
if 'a' in name:
    print('Да, она содержит строку "a"')
if name.find('war') != -1:
    print('Да, она содержит строку "war"')

delimiter = '_*_'
mylist = ['Бразилия', 'Россия', 'Индия', 'Китай']
print(delimiter.join(mylist))

# Вывод:
# $ cp prog/str_methods.py str_methods.py
# $ python3 str_methods.py

help(str)


print("\n--- End ---")
