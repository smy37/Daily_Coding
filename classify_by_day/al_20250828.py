import sys

### First Approach
# def cal_current(no_skip, skip, choice):
#     num = int(choice[1:])
#     if choice[0] == "+":
#         skip = max(no_skip, skip+num)
#         no_skip += num
#     elif choice[0] == "*":
#         skip = max(no_skip, skip*num)
#         no_skip *= num
#     elif choice[0] == "-":
#         skip = max(no_skip, skip-num)
#         no_skip -= num
#     elif choice[0] == "/":
#         skip = max(no_skip, skip//num)
#         no_skip //= num
#     return no_skip, skip

def cal_current(no_skip, skip, choice):
    num = int(choice[1:])
    if choice[0] == "+":
        skip = skip+num if skip >0 else 0
        if no_skip > 0 : skip = max(no_skip, skip)
        no_skip = no_skip + num if no_skip > 0 else 0
    elif choice[0] == "*":
        skip = skip*num if skip >0 else 0
        if no_skip > 0 : skip = max(no_skip, skip)
        no_skip = no_skip * num if no_skip > 0 else 0
    elif choice[0] == "-":
        skip = skip-num if skip >0 else 0
        if no_skip > 0 : skip = max(no_skip, skip)
        no_skip = no_skip - num if no_skip > 0 else 0
    elif choice[0] == "/":
        skip = skip//num if skip >0 else 0
        if no_skip > 0 : skip = max(no_skip, skip)
        no_skip = no_skip//num if no_skip > 0 else 0
    return no_skip, skip


N = int(sys.stdin.readline())
no_skip = 1
skip = 0 
flag = True
for _ in range(N):
    choices = list(sys.stdin.readline().split())
    left_no_skip , left_skip = cal_current(no_skip, skip, choices[0])
    right_no_skip , right_skip = cal_current(no_skip, skip, choices[1])
    
    no_skip = max(left_no_skip, right_no_skip)
    skip = max(left_skip, right_skip)
    if no_skip <= 0 and skip <= 0:
        flag = False
        break
    
if not flag:
    print("ddong game")
else:
    print(max(no_skip, skip))


explain="""
처음 시도에서 테스트 케이스로 주어지는 거의 모든 케이스에 대하여 통과를 했지만
이미 skip을 해야만 해서 no_skip 경로가 죽어버렸는데도 해당 경로를 나중에 살려서 사용하는 
케이스가 존재하였다. 따라서 두번째 시도처럼 현재 죽은 경로인지 판단해서 죽은경로라면
다시 살리지 않는 로직으로 바꿨다.
"""