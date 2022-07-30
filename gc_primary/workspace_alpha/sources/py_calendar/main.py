from gcpaths import *
from datetime import date

year = {}
n = date.today().year
# year[n] = open(f'{patha}\\samples\\years\\{n}.txt', 'a')
# year[n].close() #nothing

year[n] = open(f'{patha}\\samples\\years\\{n}.txt', 'r')
lines = year[n].readlines()
row = []
for line in lines:
    row.append(line.strip().split('.'))

print('m\d 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1')
for i in range(12):
    print(' '.join(row[i]))
