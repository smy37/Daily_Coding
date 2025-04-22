import sys

a,b,c,d = map(int, sys.stdin.readline().split())
a2,b2,c2,d2 = map(int, sys.stdin.readline().split())

print(f'[[{a},{b}],[{c},{d}]], [[{a2},{b2}],[{c2},{d2}]]')