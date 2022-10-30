'''Задача 2. Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.'''
from random import randint

sp = []
for i in range(1, 10):
    sp.append(randint(1, 15))
print(sp)
l = int(len(sp) / 2 + 1)
sp2 = []
for i in range(l):
    sp2.append(sp[i] * sp[len(sp) - i - 1])
print(sp2)
