"""
Создайте список и введите его значения. Найдите наибольший и наименьший элемент списка,
а также сумму и среднее арифметическое его значений.
"""
import random

lst = [random.randrange(1, 1000) for i in range(0, 10)]
print(lst)
print("Min number of the list is {}".format(min(lst)))
print("Max number of the list is {}".format(max(lst)))
print("Average of the list is {}".format(sum(lst) / len(lst)))

