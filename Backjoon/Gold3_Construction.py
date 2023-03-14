import sys

T = int(sys.stdin.readline())
for _ in range(T):
    build_order = []
    N, K = map(int, sys.stdin.readline().strip().split(' '))

    time_list = list(map(int, sys.stdin.readline().strip().split(' ')))

    for _ in range(K):
        build_order.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    obj = int(sys.stdin.readline())

    build_dic = {}
    time_dic = {}
    for i in range(1, N+1):
        time_dic[i] = 0
        build_dic[i] = {}

    for i in build_order:
        build_dic[i[1]][i[0]] = 1

    sensor = True
    while sensor:
        del_list = []
        for i in build_dic:
            if len(build_dic[i]) == 0:
                time_dic[i] += time_list[i-1]
                if i == obj:
                    sensor = False
                    break
                for j in build_dic:
                    if i in build_dic[j]:
                        build_dic[j].pop(i)
                        time_dic[j] = max(time_dic[j], time_dic[i])
                del_list.append(i)

        for i in del_list:
            build_dic.pop(i)

    print(time_dic[obj])