import sys

entire = sys.stdin.readline().rstrip().split('-')

temp = sum(list(map(int,entire[0].rstrip().split('+'))))

for i in entire[1:]:
    temp -= sum(list(map(int, i.rstrip().split('+'))))
print(temp)