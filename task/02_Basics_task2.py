# -*- coding: utf-8 -*- 

# для самопроверки после блока '/ ...code... /'
# удалите код, если он есть, и выполните задание повторно


## Вывод на экран

# Создайте 2 строковые переменные, присвоив им некоторые знечения: s1, s2
# / ...code... /
s1 = 'qwerty'
s2 = "Word"

# Объедините их в виде третей переменной res:
# / ...code... /
res = s1 + s2

# Выведите на экран значение res:
# / ...code... /
print(res)

# Создайте 2 числовые переменные, присвоив им некоторые знечения: a, b
# / ...code... /
a = 2
b = 3

# Найдите их сумму в виде третей переменной с:
# / ...code... /
c = a + b

# Выведите на экран значение с:
# / ...code... /
print(c)

# Вывод на экран 6 переменных в 1 стороку, объединив их с помощью оператора '+'
# / ...code... /
print(s1 + s2 + res + str(a) + str(b) + str(c))

# Для переменных a, b, c напишите вывод на экран методом format
# / ...code... /
print('a = {}, b = {}, c = {}'.format(a, b, c))

# Для переменных s1, s2, res напишите вывод с использованием спец. символов
# / ...code... /
print("s1 = %s, s2 = %s, res = %s" % (s1, s2, res))

# Вывод на экран переменной res c тремя знаками равно в начале и конце
# с центровкой текста (^) по ширине:
# / ...code... /
print('{0:=^{le}}'.format(res, le = len(res) + 6))

# Для переменных a, b, c напишите вывод на экран методом format по ключевым словам
# / ...code... /
print('var1 = {v1}, var2 = {v2}, var1 + var2 = {v3}'.format(v1 = a, v2 = b, v3 = c))

# Для a, b, s1, s2 напишите вывод на экран методом format
# / ...code... /
print('a = {}, b = {}, s1 = {}, s2 = {}'.format(a, b, s1, s2))

# Найти деление числа 45 на 9.7 и вывести на экран его значение 
# с точностью в 5 знаков после запятой (точки):
# / ...code... /
print('{0:.6}'.format(45 / 9.7))