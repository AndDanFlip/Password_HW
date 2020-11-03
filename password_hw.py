import os

os.system('cls')

a = input('Введите пароль: ')
length = len(a)

check = 8

try:
    div = check/length

    div = int(div)

    print('Ваш пароль состоит только из цифр')
except ZeroDivisionError:
    print('Вы ввели пустой пароль')
except ValueError:
    print('Требования к паролю соблюдены') 
