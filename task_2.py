# Посчитать четные и нечетные цифры введенного натурального числа. Например, если
# введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
x = int(input('Введите натуральное число любой длины: '))

DIVIDER = 10
even_numbers = 0
odd_numbers = 0

while x >= 1:
    number = x % DIVIDER
    x //= DIVIDER
    if number % 2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1



print(f'Четных чисел: {even_numbers}')
print(f'Нечётных чисел: {odd_numbers}')

# https://drive.google.com/file/d/1bxdkxdjbK5VGZC8G1FKRimQTuOOHx7_s/view?usp=sharing