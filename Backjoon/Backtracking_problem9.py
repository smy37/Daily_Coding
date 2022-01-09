import sys

iter = int(sys.stdin.readline())

syn_list = []
for i in range(iter):
    temp = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    syn_list.append(temp)

def Combination(n):
    target = int(n/2)
    result = []
    indice = list(range(target))
    result.append([w for w in indice])
    while True:
        for i in reversed(range(target)):
            if indice[i] != n-target + i:
                break
        else:
            return result
        indice[i] += 1
        for j in range(i+1, target):
            indice[j] = indice[j-1] +1
        result.append([w for w in indice])


temp = Combination(len(syn_list))


min = 10000000
for i in temp:
    adversial = [x for x in range(len(syn_list)) if x not in i]
    temp_sum = 0
    adversial_sum = 0
    for j in range(len(i)):
        for k in range(j+1, len(i)):
            temp_sum+= syn_list[i[j]][i[k]]
            temp_sum+= syn_list[i[k]][i[j]]
    for a in range(len(adversial)):
        for b in range(a+1, len(adversial)):
            adversial_sum+= syn_list[adversial[a]][adversial[b]]
            adversial_sum+= syn_list[adversial[b]][adversial[a]]
    if min > abs(temp_sum-adversial_sum):
            min = abs(temp_sum-adversial_sum)

print(min)