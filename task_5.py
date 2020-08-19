# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером
# 32 и заканчивая 127-м включительно. Вывод выполнить в табличной форме: по
# десять пар "код-символ" в каждой строке.
first = 32
last = 127


def print_ascii_symbols(start, stop):
    if start == stop:
        return f'{start} - {chr(start)}'
    elif start % 10 == 1:
        return f'{start} - {chr(start)}\n{print_ascii_symbols(start + 1, stop)}'
    else:
        return f'{start} - {chr(start)} {print_ascii_symbols(start + 1, stop)}'


a = print_ascii_symbols(first, last)
print(a)
