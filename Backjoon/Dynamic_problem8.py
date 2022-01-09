

# special = [4, 10, 28, 82, 244, 730, 2188, 6562, 19684, 59050, 177148, 531442]
# special2 = [i+1 for i in special]
# print(special2)
#
# def Make1(n):
#     cnt = 0
#     while n !=1:
#         if n in special:
#             n -=1
#             cnt+=1
#         elif n in special2:
#             n -=2
#             cnt+=2
#         elif n %3 == 0:
#             n /= 3
#             cnt+=1
#         elif n%2 == 0:
#             n/= 2
#             cnt+=1
#         else:
#             n -=1
#             cnt+=1
#     return cnt



import sys

def Make1_2(n):
    temp = [n]
    cnt = 0
    censor = True
    while censor :
        temp2 = []
        for i in temp:
            if i == 1:
                censor = False
                return cnt
            if i%3 ==0:
                temp2.append(int(i/3))
            if i%2 == 0:
                temp2.append(int(i/2))
            temp2.append(i-1)
        cnt+=1
        temp = temp2

temp_num = int(sys.stdin.readline())
print(Make1_2(temp_num))