#Author = Varfolomeev Nikita Denisovich
#Group = P3112
#Date = 05.10.2025
#3
from re import*

with open('Informatics_Lab3_Task1_test', 'r') as file:
    lines = file.readlines()
reg = r'([А-Я][а-я]+|[А-Я][а-я]+-[А-Я][а-я]+) [А-Я]\.[А-Я]\.'
itog = findall(reg, lines[0])
print(sorted(itog))