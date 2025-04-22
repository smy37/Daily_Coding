import sys


def find_best(num_list : list):
    cri_h  = max(num_list[1:])
    final_max = 0
    for i in range(cri_h, 0, -1):
        temp_result = 0
        temp_max = 0
        try:
            temp_start = num_list[1:].index(i)
        except:
            continue
        for j in range(temp_start, len(num_list)):
            if num_list[j] >= i  :
                temp_max += 1

            else:
                if temp_result < temp_max:
                    temp_result = temp_max
                temp_max = 0
        if final_max < i*(max(temp_max,temp_result)):
            final_max = i*(max(temp_max,temp_result))
        if final_max >= (i-1)*(len(num_list)-1):
            break
    return final_max


if __name__ == "__main__":
    temp = list(map(int, sys.stdin.readline().split(' ')))

    while temp[0] != 0:

        print(find_best(temp))
        temp = list(map(int, sys.stdin.readline().split(' ')))
