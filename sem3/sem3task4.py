'''Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Нельзя использовать готовые функции.'''

n = int(input())
b = ''

while n > 0:
    b = str(n % 2) + b
    n = n // 2

print(b)
