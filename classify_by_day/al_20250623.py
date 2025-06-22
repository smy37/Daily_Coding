import sys 

N = int(sys.stdin.readline())

### 1. First Try (Wrong Method)
# for _ in range(N):
#     t_str = sys.stdin.readline().strip()
#     s, e = 0, len(t_str)-1

#     flag_0 = True
#     flag_1 = True
#     flag_2 = False

#     for _ in range(len(t_str)//2):
#         if t_str[s] != t_str[e]:
#             flag_0 = False
#             if flag_1:
#                 flag_1 = False
#                 if t_str[s+1] == t_str[e]:
#                     s = s+1
#                 elif t_str[s] == t_str[e-1]:
#                     e = e-1
#                 else:
#                     flag_2 = True
#                     break
#             else:
#                 flag_2 = True
#                 break
#         s += 1
#         e -= 1

#     if flag_0:
#         print(0)
#     elif flag_2:
#         print(2)
#     else:
#         print(1)


### 2. Second Try 
def check_palin(string):
    for i in range(len(string)//2):
        if string[i] != string[len(string)-1-i]:
            return False
    return True

for _ in range(N):
    t_str = sys.stdin.readline().strip()
    s, e = 0, len(t_str)-1

    for _ in range(len(t_str)//2):
        if t_str[s] != t_str[e]:
            if check_palin(t_str[s+1:e+1]) or check_palin(t_str[s:e]):
                print(1)
                break
            else:
                print(2)
                break
        s += 1
        e -= 1
    else:
        print(0)


explain = """
첫번째 방법은 문자를 하나 지울때, if else 문으로 접근하므로 s쪽을 지우든 e쪽을 지우든 지우게 되면 통과 가능하고 최종적으로 회문이 되려면
e쪽을 지웠어야 했을 때, 문제를 야기한다. 따라서 두번째 접근에서는 지워야 되는 상황에서 앞쪽을 지운경우와 뒷쪽을 지운 경우에 대해서 회문 검사를
시행해줌으로써 풀 수 있었다. 사실, 첫번째 방법 작성시에 해당 엣지케이스를 떠올렸는데 아래처럼 하는게 시간 초과를 발생시킬지도 모른다는 우려가 있었지만
다행히 시간 초과는 발생시키지 않았다. 
"""