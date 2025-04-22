inputs = ["100110", "1101", "1001111"]

def autocompletes(inputs):
    # Write your code here
    stack = []
    for i in range(len(inputs)):
        max_v = 0
        max_idx = 0
        for j in range(i):
            cri = min(len(inputs[i]), len(inputs[j]))
            a = inputs[i][:cri]
            b = inputs[j][:cri]
            cnt = 0
            for k in range(cri):
                if a[k] != b[k]:
                    break
                else:
                    cnt +=1
            print(a,b,cnt)
            if cnt >= max_v:
                max_v = cnt
                max_idx = j+1
        if i == 0:
            stack.append(0)
        else:
            stack.append(max_idx)
    return stack

print(autocompletes(inputs))
cur = 2
can_l = [i for i in [1,2,3] if i!=cur]
print(can_l)