# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
#  является ли этот день выходным.

a = int(input('Введите цифру дня недели '))
if a == 6 or a == 7:
    print(f'{a} - выходной день')
else:
    print(f'{a} будний день')
