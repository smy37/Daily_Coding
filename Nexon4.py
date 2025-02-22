def cal_aval(initailEnergy, time, th):
    temp = 0
    for i in initailEnergy:
        temp += max(i - time, 0)
    if temp >= th:
        return True
    else:
        return False


def GetMaxTime(initialEnergy, th):
    # Write your code here
    n = len(initialEnergy)
    s = 0
    e = max(initialEnergy)
    m = (s + e) // 2

    while s != m:
        if cal_aval(initialEnergy, m, th):
            s = m
            m = (s + e) // 2
        else:
            e = m - 1
            m = (s + e) // 2
    if cal_aval(initialEnergy, e, th) == True:
        return e
    else:
        return s

ie = [3,9,7,6]
th = 6

print(GetMaxTime(ie, th))