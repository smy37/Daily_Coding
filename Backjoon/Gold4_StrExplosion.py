import sys

string = sys.stdin.readline().strip()
boom = sys.stdin.readline().strip()

s = []

for i in range(len(string)):
    s.append(string[i])
    if s[-1] == boom[-1] and len(s) >= len(boom) and boom == ''.join(s[-len(boom):]):
        del s[-len(boom):]
if len(s)>0:
    print(''.join(s))
else:
    print("FRULA")