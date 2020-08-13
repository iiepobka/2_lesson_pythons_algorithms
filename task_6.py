# В программе генерируется случайное целое число от 0 до 100. Пользователь
# должен его отгадать не более чем за 10 попыток. После каждой неудачной попытки
# должно сообщаться, больше или меньше введенное пользователем число, чем то,
# что загадано. Если за 10 попыток число не отгадано, вывести правильный ответ.
from random import randint

print('Отгадайте число от 0 до 100')
random_number = randint(0, 100)
try_count = 10
# print(random_number)


def guess_the_number(count):
    if count > 0:
        user_input = int(input(f'Введите целое число от 0 до 100 (у вас {count} попытки(a|ок)): '))
        if user_input > random_number:
            print('Ваше число больше загаданного')
            return guess_the_number(count - 1)
        elif user_input < random_number:
            print('Ваше число меньше загаданного')
            return guess_the_number(count - 1)
        else:
            return f'Вы отгадали!\nПотрачено {try_count - count + 1} попытка(и|ок)'
    else:
        return f'Вы проигради!\nБыло загадано число: {random_number}'


g = guess_the_number(try_count)
print(g)
