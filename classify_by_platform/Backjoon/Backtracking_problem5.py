import sys

num = int(sys.stdin.readline())



def countS(sol, n):
    global cnt
    if len(sol) == n:
        cnt += 1
        return 0

    candidate = list(range(n))
    for i in range(len(sol)):
        if sol[i] in candidate:
            candidate.remove(sol[i])
        distance = len(sol)- i
        if sol[i] + distance in candidate:
            candidate.remove(sol[i]+distance)
        if sol[i] - distance in candidate:
            candidate.remove(sol[i]-distance)
    if candidate != []:
        for i in candidate:
            sol.append(i)
            countS(sol, n)
    else:
        return 0
cnt = 0
for i in range(num):
    countS([i],num)
print(cnt)