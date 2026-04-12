import sys

memory = {}

def folding(left, right):
    if left == right:
        memory["0"] = True
        memory["1"] = True
        return ["0", "1"]

    mid = (left+right)//2
    right_side_list = folding(mid+1, right)
    cur_comb = []
    for right_side in right_side_list:
        reverse = right_side[::-1]
        mod_reverse = []
        for s in reverse:
            if s == "1":
                mod_reverse.append("0")
            else:
                mod_reverse.append("1")
        reverse = "".join(mod_reverse)
        new_comb = reverse + "0" + right_side
        new_comb_2 = reverse + "1" + right_side
        if new_comb not in memory:
            memory[new_comb] = True
        if new_comb_2 not in memory:
            memory[new_comb_2] = True
        cur_comb.append(new_comb)
        cur_comb.append(new_comb_2)

    return cur_comb


T = int(sys.stdin.readline())

for _ in range(T):
    target = sys.stdin.readline().strip()
    if target in memory:
        print("YES")
        continue
    left, right = 0, len(target)-1
    folding(left, right)

    if target in memory:
        print("YES")
    else:
        print("NO")