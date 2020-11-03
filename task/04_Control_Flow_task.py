# -*- coding: utf-8 -*- 

# для самопроверки после блока '/ ...code... /'
# удалите код, если он есть, и выполните задание повторно


# Оператор if
# / ...code... /
t = int(input('Какая сегодня температура: '))
if t > 30:
    s = 'очень жарко'
elif t > 20:
    s = 'жарко'
elif t > 10:
    s = 'тепло'
elif t > 0:
    s = 'слегка тепло'
elif t > -10:
    s = 'прохладно'
else:
    s = 'начинается мороз'

print('На улице температура %s, это значит %s' % (t, s))

# Оператор while
# / ...code... /
max = int(input('Введите положительное целое число менее 50: '))
s, r = 0, 1
while s < max:
    s += 1
    r = 1 + 1 / r
    print('%s: r = %s' % (s, r))
print('Число Фибоначчи на {} шаге составило {}'.format(s, r))

# Цикл for
# / ...code... /
max = int(input('Введите положительное целое число менее 50: '))
s = 0
for i in range(max, 0, -1):
    s += i
    print(i)
print('summa =', s)

# Оператор break
# / ...code... /
max = int(input('Введите положительное целое число менее 50: '))
s = 0
for i in range(1, 25):
    if i == max:
        break
    s += i
    print(i)
print('summa =', s)

# Оператор continue
# / ...code... /
max = int(input('Введите положительное целое число менее 50: '))
s = 0
for i in range(max, 0, -1):
    if i % 2 == 1:
        continue
    s += i
    print(i)
print('summa =', s)

# Оператор if и операторы and, or, not 
# / ...code... /
t = int(input('Какая сегодня температура: '))
if t > 100 or t < -100:
    s = 'очень странно'
elif t > 30:
    s = 'жарко'
elif t > 10:
    s = 'тепло'
elif t > 0:
    s = 'слегка тепло'
elif t > -10:
    s = 'прохладно'
else:
    s = 'начинается мороз'
print('На улице температура %s, это значит %s' % (t, s))

# Цикл for с шагом 2
# / ...code... /
max = int(input('Введите положительное целое число менее 50: '))
s = 0
for i in range(0, max, 2):
    s += i
    print(i)
print('summa =', s)


print("\n--- End ---")
