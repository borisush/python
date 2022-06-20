"""
Простым называется число, которое делится нацело только на единицу и само себя.
Число 1 не считается простым. Напишите программу, которая находит все простые числа
в заданном промежутке, выводит их на экран, а затем по требованию пользователя выводит
их сумму либо произведение.
"""

start = int(input("Please enter the first number in your range: "))
end = int(input("Please enter the last number in your range: "))
primes = []
total = 1

for i in range(start, end):
    prime = True

    for j in range(2, i-1):
        if i % j == 0:
            prime = False
            break

    if i == 1 or i == 2:
        continue

    if prime:
        primes.append(i)

print(primes, "\n")

operation = int(input("Enter 1 if you want to find the sum of these numbers, " \
                      "or 2 if you want to multiply them: "))
if operation == 1:
    print("The sum of all numbers in the list is {}.".format(sum(primes)))
elif operation == 2:
    for item in primes:
        total = total * item
    print("The product of all numbers in the list is {}.".format(total))

