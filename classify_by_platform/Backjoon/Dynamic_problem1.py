import sys

def fiboC01(n):
    num_list = []
    for i in range(n+1):
        num_list.append([0,0])

    if n!=0:
        num_list[0][0]=1
        num_list[1][1]=1
    elif n==0:
        num_list[0][0]=1
    for j in range(2,n+1):
        num_list[j][0] += num_list[j-1][0] + num_list[j-2][0]
        num_list[j][1] += num_list[j-1][1] + num_list[j-2][1]

    return num_list[-1]

iterate = int(sys.stdin.readline())
for i in range(iterate):
    number = int(sys.stdin.readline())
    temp = fiboC01(number)
    print(temp[0], temp[1])
