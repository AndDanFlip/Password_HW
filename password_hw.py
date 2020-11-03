import os

os.system('cls')

a = input('Введите пароль: ')
length = len(a)

check = 8
a = int(a)

try:
    div = check/length
except ZeroDivisionError:
    print('Вы ввели пустой пароль')
except ValueError:
    print('Требования к паролю соблюдены') 
print('Ваш пароль состоит только из цифр')