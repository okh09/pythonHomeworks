'''Задача 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
 стоящих на нечётной позиции.'''

from random import randint

sp = []
for i in range(1, 10):
    sp.append(randint(1, 30))
print(sp)
l = len(sp)

nechet = []
for i in range(l):
    if i % 2 != 0:
        nechet.append(sp[i])
print('На нечетных позициях элементы:', nechet, ', ответ:', sum(nechet))
