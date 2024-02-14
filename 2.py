import csv

with open('space.txt', 'r') as file:
    rows = file.readline()
    f = list(csv.reader(file, delimiter='*'))
for i in range(1, len(f)):
    for j in range(i, 0, -1):
        if int(f[j][0][5::]) < int(f[j - 1][0][5::]):
            f[j - 1], f[j] = f[j], f[j - 1]
        else:
            break
for k in range(10):
    print(f[k][0])
