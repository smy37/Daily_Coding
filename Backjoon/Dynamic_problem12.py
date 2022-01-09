import sys

num_length = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().rstrip().split()))


final_result = 0
for i in range(num_length):
    temp_1 = {}
    temp_2 = {}
    for j in range(i+1):
        temp_2[j+1] = []
    for j in range(num_length-i):
        temp_1[j+1] = []

    temp_1[1].append(num_list[i])
    temp_2[1].append(num_list[i])

    r_curl = 1
    l_curl = 1
    for j in range(i+1, num_length):
        if temp_1[r_curl][0] > num_list[j]:
            r_curl += 1
            temp_1[r_curl].append(num_list[j])
        else:
            for k in range(r_curl):
                if k != 0:
                    if temp_1[k+1][0] < num_list[j] and temp_1[k][0] > num_list[j]:
                        temp_1[k+1][0] = num_list[j]
                        break
                else:
                    if temp_1[k+1][0] <num_list[j]:
                        temp_1[k+1][0] = num_list[j]

    for j in range(i-1, -1, -1):
        if temp_2[l_curl][0] > num_list[j]:
            l_curl += 1
            temp_2[l_curl].append(num_list[j])
        else:
            for k in range(l_curl):
                if k != 0:
                    if temp_2[k+1][0] < num_list[j] and temp_2[k][0] > num_list[j]:
                        temp_2[k+1][0] = num_list[j]
                        break
                else:
                    if temp_2[k+1][0] < num_list[j]:
                        temp_2[k+1][0] = num_list[j]
                        break

    if r_curl+l_curl-1 > final_result:
        final_result = r_curl+l_curl-1

print(final_result)

