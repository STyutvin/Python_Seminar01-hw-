# Задача №1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
day=int(input('Введите число, обозначающую день недели, от 1 до 7: '))
if day < 1 or day >7:
    print('Число введено некорректно.')
elif day==6 or day==7:
    print('Это выходной.')
else:
    print('Это рабочий день.')
