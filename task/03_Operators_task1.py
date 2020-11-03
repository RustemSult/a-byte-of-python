# -*- coding: utf-8 -*- 

## Операторы

## Что делают данные операторы?
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
# '^' 
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

# Проверка операции

a, b = 10, 3

print("Оператор '**' между {} и {} дает результат:".format(a, b), (a ** b))

print("Оператор '//' между {} и {} дает результат:".format(a, b), (a // b))

print("Оператор '%' между {} и {} дает результат:".format(a, b), (a % b))

print("Оператор '<<' между {} и {} дает результат:".format(a, b), (a << b))
print("Оператор '>>' между {} и {} дает результат:".format(a, b), (a >> b))

print("Оператор '&' между {} и {} дает результат:".format(a, b), (a & b))
print("Оператор '|' между {} и {} дает результат:".format(a, b), (a | b))
print("Оператор '^' между {} и {} дает результат:".format(a, b), (a ^ b))
print("Оператор '~' для {} дает результат:".format(a), (~ a))
print("Оператор '~' для {} дает результат:".format(b), (~ b))

a, b = True, False

print("Оператор 'not' для {} дает результат:".format(a), (not a))
print("Оператор 'not' для {} дает результат:".format(b), (not b))
print("Оператор 'and' между {} и {} дает результат:".format(a, b), (a and b))
print("Оператор 'or' между {} и {} дает результат:".format(a, b), (a or b))


print("--- End ---")