# Сформировать из введенного числа обратное по порядку входящих в него цифр и
# вывести на экран. Например, если введено число 3486, надо вывести 6843.

number = int(input('Введите натуральное число любой длины: '))

CONSTANT = 10
reversed_number = 0

while number >= 1:
    reversed_number = (reversed_number * CONSTANT) + (number % CONSTANT)
    number //= CONSTANT

print(reversed_number)
