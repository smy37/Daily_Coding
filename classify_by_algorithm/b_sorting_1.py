import sys


def divide_sort(n_list : list) :
    def _merge(A: list, B: list):
        f_cnt = 0
        cnt1 = 0
        cnt2 = 0
        temp = []
        while f_cnt != len(A) + len(B):
            if cnt1 == len(A):
                temp.append(B[cnt2])
                cnt2 += 1
                f_cnt += 1
            elif cnt2 == len(B):
                temp.append(A[cnt1])
                cnt1 += 1
                f_cnt += 1
            elif A[cnt1] <= B[cnt2]:
                temp.append(A[cnt1])
                cnt1 += 1
                f_cnt += 1
            elif A[cnt1] > B[cnt2]:
                temp.append(B[cnt2])
                cnt2 += 1
                f_cnt += 1
        return temp

    if len(n_list) == 1:
        return n_list

    else:
        cri = len(n_list)//2
        temp1 = n_list[0:cri]
        temp1 = divide_sort(temp1)
        temp2 = n_list[cri:len(n_list)]
        temp2 = divide_sort(temp2)
        return _merge(temp1, temp2)

if __name__ == "__main__" :
    iter_n = int(sys.stdin.readline())
    num_list = []

    for i in range(iter_n):
        num_list.append(int(sys.stdin.readline()))

    result = divide_sort(num_list)

    for i in result:
        print(i)