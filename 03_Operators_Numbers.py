# -*- coding: utf-8 -*- 


print("--- Числа ---\n")


## Числа

5 + 5
5 - 5
5 * 5
5 ** 5

5 ** 2
5 / 2

10 / 2

10 // 2
11 // 2

11 % 2
11 % 4

a = 5

# Вывод на экран операций с переменной a
print("5 + 5 =", a + a)
print("5 - 5 =", a - a)
print("5 * 5 =", a * a)
print("5 ** 5 =", a ** a)

# Вывод на экран проводимой операции и его результата
print("5 / 2 =", 5 / 2)
print("11 / 4 =", 11 / 4)
print("11 // 4 = ", 11 // 4)
print("11 % 4 = ", 11 % 4)

print("10 >> 2 = ", 10 >> 2)
print("10 << 2 = ", 10 << 2)

print("11 & 5 = ", 11 & 5)
print("11 | 5 = ", 11 | 5)
print("11 ^ 5 = ", 11 ^ 5)

print("\n--- Комплексные числа ---\n")
a = 3 + 2j
print("Комплексное число a: ", a)


## Метод int()

print("\n--- Метод int() ---\n")

a = 1.25
i = int(a)
print(i)

b = 1 / 7
print(int(b))

a *= 3
print("Это число '{}' и её целая часть равна {}".format(a, int(a)))

b += 2
print("Это число '{}' и её целая часть равна {}".format(b, int(b)))
print("Это число '{}' и её дробная часть равна {}".format(b, b-int(b)))


print("\n--- End ---")
