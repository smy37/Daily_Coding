import sys

def get_recur(cur_num, depth):
    if depth == 0:
        return [[cur_num]]
    cur_num_l = []
    for i in range(cur_num-1, -1, -1):
        recur_num_l = get_recur(i, depth-1)
        for comb in recur_num_l:

            cur_num_l.append([cur_num]+comb)
    return cur_num_l

N = int(sys.stdin.readline())
if N <= 9:
    print(N-1)
    sys.exit()

comb_num_list = []
for i in range(1, 11):
    temp = 1
    for j in range(i):
        temp *= (10-j)/(i-j)
    comb_num_list.append(round(temp))

cri = sum(comb_num_list)
if N > cri:
    print(-1)
else:
    accum_val = 0
    for idx in range(len(comb_num_list)):
        accum_val += comb_num_list[idx]

        if N <= accum_val:
            break
    target = accum_val- N + 1

    answer = None
    temp_accum = 0
    for i in range(9, 0, -1):
        cur_num_l = get_recur(i, idx)

        temp_accum += len(cur_num_l)

        if target <= temp_accum:
            rest = (temp_accum-target)+1

            answer = cur_num_l[-rest]

            break
    print(int("".join(map(str, answer))))

