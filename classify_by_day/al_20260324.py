import sys

dist = int(sys.stdin.readline())
nano = 10**7
while dist:
    dist *= nano
    n = int(sys.stdin.readline())
    num_list = []
    flag = False
    for _ in range(n):
        t = int(sys.stdin.readline())
        num_list.append(t)
    num_list.sort()

    left, right = 0, n-1

    while left < right:
        cur_dist = num_list[left] + num_list[right]

        if cur_dist > dist:
            right -= 1
        elif cur_dist < dist:
            left += 1
        else:
            print("yes", num_list[left], num_list[right])
            flag = True
            break
    if not flag: print("danger")

    try:
        dist = int(sys.stdin.readline())
    except:
        break
