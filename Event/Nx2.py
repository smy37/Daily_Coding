def minimumMovement(obstacleLanes):
    # Write your code here
    cnt = 0
    n = len(obstacleLanes)
    cur = 2
    c_l = [1, 3]
    cri = 0
    for i in range(n):
        if obstacleLanes[i] != cur:
            continue
        else:
            cri = i + 1
            cnt += 1
            break
    if cri == n:
        cnt = 0

    while cri < n:
        flag1 = False
        flag2 = False
        for i in range(cri, n):
            if obstacleLanes[i] in c_l and flag1 == False:
                flag1 = True
                c_l.remove(obstacleLanes[i])
            elif obstacleLanes[i] in c_l and flag1 == True:
                flag2 = True
                cri = i + 1
                cnt += 1
                cur = obstacleLanes[i]
                c_l = [j for j in [1, 2, 3] if j != cur]
                break
        if flag2 == False:
            break
    return cnt
a = [2,3,2,1,3,1]

print(minimumMovement(a))