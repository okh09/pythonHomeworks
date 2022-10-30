'''Задача 3. Задайте список из вещественных чисел. Напишите программу,
которая найдёт разницу между максимальным и минимальным значением дробной части элементов.'''

sp = [float(i) for i in input().split()]

print(sp)
dr = []

for i in sp:
    dr.append(i % 1)

maximum = -1001
minimum = 1001
for i in dr:
    if i > maximum:
        maximum = i
for i in dr:
    if i < minimum:
        minimum = i


def result():
    return maximum - minimum


print(round(result(), 2))
