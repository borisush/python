"""
Задание 2

Перепишите решение последней задачи из шестого урока так, чтобы она не использовала рекурсию
и не вычисляла все промежуточные количества вариантов путей множество раз (что крайне неэффективно),
а сохраняла их в списке.
"""

index = int(input('Enter the number of steps on a ladder: '))
steps = [1, 1]

for i in range(index - 2):
    steps.append(steps[i] + steps[i + 1])

print(steps)