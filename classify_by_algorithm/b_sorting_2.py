import sys

iter_num = int(sys.stdin.readline())

num_list = []

for i in range(iter_num):
    num_list.append(int(sys.stdin.readline()))


def divide_sort(nlist : list):
    if len(nlist) == 1:
        return nlist

    else:
        cri = len(nlist)//2
        temp1 = nlist[0:cri]
        temp1 = divide_sort(temp1)
        temp2 = nlist[cri:len(nlist)]
        temp2 = divide_sort(temp2)
        temp_result = merge(temp1, temp2)

        return temp_result



def merge(A, B):
    result = []
    cnt1 = 0
    cnt2 = 0
    cnt = 0
    while cnt != len(A)+ len(B):
        if cnt1 == len(A) :
            result.append(B[cnt2])
            cnt2+=1
        elif cnt2 == len(B):
            result.append(A[cnt1])
            cnt1+=1
        elif A[cnt1] <= B[cnt2]:
            result.append(A[cnt1])
            cnt1+=1
        elif A[cnt1] > B[cnt2]:
            result.append(B[cnt2])
            cnt2+=1
        cnt +=1

    return result


if __name__ == "__main__":
    for i in divide_sort(num_list):
        print(i)