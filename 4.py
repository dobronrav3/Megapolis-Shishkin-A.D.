import csv

def psw(n):
    '''
    Функция генерирует пароль согласно установленным правилам
    :param n: Данные о корабле
    :return: Пароль
    '''
    password = (n[1][-3::] + n[0][2] + n[0][1] + n[1][:3][::-1]).upper()
    return password

with open('space.txt', 'r') as file:
    rows = file.readline()[0:-1] + '*password\n'
    f = list(csv.reader(file, delimiter='*'))
for i in f:
    i.append(psw(i))
with open('space_uniq_password.csv', 'w') as new_file:
    new_file.write(rows)
    for i in f:
        s = '*'.join(i) + "\n"
        new_file.write(s)
print(rows)