"""
Создайте список, введите количество его элементов и сами значения,
выведите эти значения на экран в обратном порядке.
"""

lst = []
elements = int(input("Enter the number of elements you want to have in your list: "))
for i in range(elements):
    number = int(input("Enter the {} element of the list: ".format(i)))
    lst.append(number)

for i in reversed(range(len(lst))):
    print(lst[i])
