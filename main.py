from ipaddress import ip_address
from pickle import TRUE
from random import vonmisesvariate
from tkinter import X
from xmlrpc.client import TRANSPORT_ERROR


print("putin eat more shit")
#putin = "vor"    
#hwoh = 666
#print(putin, hwoh)
# inp = input()
# print(inp + " " + putin)
#x = 2
#y = 3
#print (f'{x}{y}')
#print(x + y)
# при запуски программы ввожу любую строку, вывести должна "Hello, ____ !"
#input = input()
#print("Hello, " + input + "!")
#print(f"Hello, {input}!" )
# 1. Создать две переменные (числа) вывести сумму, разность, произведение и
# что нибудь разделить и корень из этих  чисел, отсаток от деления.
# 2. Числа должны вводится в командной строке.
# print("vvedi pervoe chislo hmir`") 
# x = float(input())
# print("vvedi vtoroe chislo hmir`")
# y = float(input())
# print(f"summma { x + y }")
# print(f"raznost { x - y }")
# print(f"delenie { x / y }")
# print(f"umnogit { x * y }")
# print(f"koren iz { x ** (0.5) } {y ** (0.5)}")
# print(f"ostatok delenie { x % y }")


# если число четное вывести принт "четное" если число не четное "вывести нечетное"
while True:
    print("Введи число")
    y = input()
    if y == "exit":
        break
    x = float(y)
    if x % 2 == 0:
        print("Четное")
    else:
        print("Нечетное")