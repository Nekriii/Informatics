#Author = Varfolomeev Nikita Denisovich
#Group = P3112
#Date = 05.10.2025
#4
from re import*

with open('Informatics_Lab3_Task2_test', 'r') as file:
    lines = file.readlines()
data = input('Введите 3 буквы и расстояние через пробел: ').split()
letter1, letter2, letter3, dist = data[0], data[1], data[2], data[3]
reg = fr'\b{letter1}.{{{dist}}}{letter2}.{{{dist}}}{letter3}\b'
itog = findall(reg, lines[0], IGNORECASE)
print(itog)