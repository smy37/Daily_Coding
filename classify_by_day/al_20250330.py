import sys

N, r, c = map(int, sys.stdin.readline().split())
n_r = r
n_c = c
accum = 0

while N > 0:
    N -= 1
    cur_x = n_r // (2**N) * ((2**N)**2) * 2
    cur_y = n_c // (2**N) * ((2**N)**2)
    accum += cur_x+cur_y
    n_r = n_r % (2**N)
    n_c = n_c % (2**N)

print(accum)
