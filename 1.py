import csv

with open('space.txt', 'r') as file:
    rows = file.readline()
    f = list(csv.reader(file, delimiter='*'))
for i in f:
    if 0 in list(map(int, i[-2].split())):
        n = int(i[0][5])
        m = int(i[0][6])
        t = len(i[1])
        xd, yd = map(int, i[-1].split())
        if n > 5:
            x = n + xd
        if n <= 5:
            x = -(n + xd) * 4 + t
        if m > 3:
            y = m + t + yd
        if m <= 3:
            y = -(n + yd) * m
        i[-2] = f'{str(x)} {str(y)}'
for i in f:
    if i[0][3] == 'V':
        print(f'{i[0]} - {tuple(map(int, i[-2].split()))}')
with open('space_new.txt', 'w') as new_file:
    new_file.write(rows)
    for i in f:
        s = '*'.join(i) + "\n"
        new_file.write(s)

