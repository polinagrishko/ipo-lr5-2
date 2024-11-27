str1=input("Введите первую строку:")
str2=input("Введите вторую строку:")
#сорттировка строк
sort_str1 = sorted(str1.lower())
sort_str2 = sorted(str2.lower())
#проверка на условие через if
if sort_str1 == sort_str2:
    print('Списки анаграммы')#вывод результата
else:
    print('Списки не анаграммы')