# -*- coding: utf-8 -*- 

print('Для завершения введите слово: выход')

while True:
    s = input('Введите что-нибудь : ')
    if s == 'выход':
        break
    print('Длина строки: ', len(s))

print('Завершение')
