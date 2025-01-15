import sys

n_port = int(sys.stdin.readline())
n_plane = int(sys.stdin.readline())
check = [i for i in range(n_port+1)]

def find(check_l, idx):
    if check_l[idx] != idx:
        temp = find(check_l, check_l[idx])
        return temp
    else:
        return check_l[idx]


def union(check_l, idx, low_idx):
    cur_idx = find(check_l, idx)
    low_idx = find(check_l, low_idx)
    check_l[cur_idx] = low_idx

answer = 0
for _ in range(n_plane):
    t = int(sys.stdin.readline())
    idx = find(check, t)

    if idx == 0:
        break
    union(check, idx, idx-1)
    answer += 1
print(answer)