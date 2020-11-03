# -*- coding: utf-8 -*- 

## Операторы

# Проверка приоритета операции

a, b, c = 10, 3, 1

# a - b + c:
print("Выражение {} - {} + {} =".format(a, b, c), (a - b + c))

# a + b * c
print("Выражение {} + {} * {} =".format(a, b, c), (a + b * c))

# a ** b + c
print("Выражение {} ** {} + {} =".format(a, b, c), (a ** b + c))


print("--- End ---")
