import sys 

N = int(sys.stdin.readline())

o1, o2 = map(int, sys.stdin.readline().split())

open_door = []
open_door.append([0]*N)
open_door[0][o1] = 1
open_door[0][o2] = 1

for _ in range(N-2):
    use_door = int(sys.stdin.readline())
    