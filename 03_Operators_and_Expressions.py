# -*- coding: utf-8 -*- 


print("--- Операторы и выражения ---\n")


## Операторы
# 
# '+'
# '-'
#
# '*'
# '**'
#
# '/'
# '//'
# 
# '%'
#
# '<<'
# '>>'
#
# '&'
# '|'
# 
# '^' 
#
# '~'
#
# '<'
# '>'
# '<=' 
# '>='
# '=='
# '!='
# 
# 'not'
# 'and'
# 'or'
# 
# #

2 + 3

3 * 5

# Вы можете записать:
a = 2; a = a * 3
# в виде:
a = 2; a *= 3

print(a)


## Порядок вычисления

# Следующая таблица показывает приоритет операторов

# Operator                    Description
#---------------------------------------------------------
# :=                          Assignment expression
#
# lambda                      Lambda expression
#
# if – else                   Conditional expression
#
# or                          Boolean OR
#
# and                         Boolean AND
#
# not x                       Boolean NOT
#
# in, not in, is, is not,     Comparisons, including membership tests and identity tests
# <, <=, >, >=, !=, ==
#
# |                           Bitwise OR
#
# ^                           Bitwise XOR
#
# &                           Bitwise AND
#
# <<, >>                      Shifts
#
# +, -                        Addition and subtraction
#
# *, @, /, //, %              Multiplication, matrix multiplication, division, floor division, remainder
#
# +x, -x, ~x                  Positive, negative, bitwise NOT
#
# **                          Exponentiation
#
# await x                     Await expression
#
# x[index], x[index:index],   Subscription, slicing, call, attribute reference
# x(arguments...), 
# x.attribute
#
# (expressions...),           Binding or parenthesized expression, list display, dictionary display, set display
# [expressions...], 
# {key: value...}, 
# {expressions...}
#
## https://docs.python.org/3/reference/expressions.html#summary

# В этой таблице операторы с равным приоритетом расположены в одной строке. 
# Например, '+' и '-' имеют равный приоритет.


## Изменение порядка вычисления

# Скобки дают возможность изменить порядок вычисления выражений:
2 + 3 * 4
# и выражение со скобками отличается в результате:
(2 + 3) * 4


## Ассоциативность

# Операторы обычно обрабатываются слева направо. Это означает, что операторы с равным
# приоритетом будут обработаны по порядку от левого до правого. Например, 2 + 3 + 4
# обрабатывается как (2 + 3) + 4 . 
# 
# Некоторые операторы, как, например, оператор присваивания, имеют ассоциативность 
# справа налево, т.е. a = b = c рассматривается как a = (b = c) .


## Выражения

length = 5
breadth = 2
area = length * breadth
print('Площадь равна', area)
print('Периметр равен', 2 * (length + breadth))


print("\n--- End ---")
