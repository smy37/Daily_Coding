import sys
import copy

N = int(sys.stdin.readline())

dset = {2:3, 3:2}
def recur_hanoi(bot, target):
    if bot == 1:
        return [1, target], [[bot, target]]
    s2t, past_hanoi = recur_hanoi(bot-1, dset[target])

    s, t = s2t
    temp_dest = {s: t, t: target}
    for i in range(1, 4):
        if i not in temp_dest:
            for j in range(1, 4):
                if j not in temp_dest.values():
                    temp_dest[i] = j
                    break
            break

    past_hanoi_2 = copy.deepcopy(past_hanoi)
    for i in range(len(past_hanoi)):
        for j in range(len(past_hanoi[i])):
            past_hanoi_2[i][j] = temp_dest[past_hanoi[i][j]]

    return [1, target], past_hanoi + [[1, target]] + past_hanoi_2

def just_cnt(cur):
    if cur == 1:
        return 1
    recur_cnt = just_cnt(cur-1)
    return recur_cnt + 1 + recur_cnt

if N <=20:
    _, record = recur_hanoi(N, 3)
    print(len(record))
    for r in record:
        print(r[0], r[1])
else:
    print(just_cnt(N))