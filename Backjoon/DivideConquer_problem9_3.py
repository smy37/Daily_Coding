import sys

start = list(map(int, sys.stdin.readline().split(' ')))


def divide_conquer(n: list):
    if len(n) == 1:
        return n[0]

    else:
        if len(n)%2 == 1:
            n = [0] + n
        cri = len(n)//2
        temp1 = n[:cri]
        temp2 = n[cri:]
        cnt1 = 0
        cnt2 = 0
        t_cri = min(temp1[cri-1-cnt1], temp2[cnt2])
        t_area = t_cri*2


        for i in range(len(temp1)+len(temp2)-2):
            if cnt1 +1 == len(temp1):
                cnt2 +=1
            elif cnt2 +1 == len(temp2):
                cnt1 +=1
            elif temp2[cnt2+1] >= temp1[len(temp1)-1-(cnt1+1)]:
                cnt2 += 1
            elif temp2[cnt2+1] < temp1[len(temp1)-1-(cnt1+1)]:
                cnt1+=1
            t_cri = min(t_cri, temp2[cnt2], temp1[len(temp1)-1-cnt1])
            t_area = max(t_area, t_cri*(2+cnt1+cnt2))
        return max(divide_conquer(temp1), divide_conquer(temp2), t_area)


while start[0] != 0:
    start = start[1:]
    print(divide_conquer(start))
    start = list(map(int, sys.stdin.readline().split(' ')))