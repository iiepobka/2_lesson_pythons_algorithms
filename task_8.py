# 8. Посчитать, сколько раз встречается определенная цифра в введенной
# последовательности чисел. Количество вводимых чисел и цифра, которую
# необходимо посчитать, задаются вводом с клавиатуры.

count_numbers = int(input('Введите целым числом количество чисел, которые будут вводиться: '))
search_number = int(input('Введите целым числом цифру, которую будем искать в водимых числах: '))
count = 0

for i in range(0, count_numbers):
    users_number = int(input(f'Введите {i + 1}-е число из {count_numbers}-х: '))
    while users_number / 10 >= 0.1:
        number = users_number % 10
        users_number //= 10
        if number == search_number:
            count += 1

print(f'Цифра {search_number} присутствовала в введенных числах {count} раз(а)')
