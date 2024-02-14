import csv

with open('space.txt', 'r') as file:
    rows = file.readline()
    f = list(csv.reader(file, delimiter='*'))
while 1:
    c = 0
    s = input()
    if s == 'stop':
        break
    for i in f:
        if s in i[0]:
            print(f'Корабль {s} был отправлен с планеты: {i[1]} и его направление движения было: {i[-1]}')
            c += 1
    if c == 0:
        print('error.. er.. ror..')