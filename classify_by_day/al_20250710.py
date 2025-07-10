import sys

input_str = sys.stdin.readline().strip()

### 1. First Approach
# stack_front = []
# stack_back = []
# for idx, v in enumerate(input_str):
#     if v == "(":
#         stack_front.append(idx)
#     elif v == ")":
#         stack_back.append(idx)
#
# if len(stack_front) == 0:
#     print(len(input_str))
#     sys.exit()
# stack_front.reverse()
#
# idx_front = stack_front[0]
# idx_back = stack_back[0]
# cur = input_str[idx_front+1:idx_back]
# cur = cur*int(input_str[idx_front-1])
#
# for i in range(1, len(stack_front)):
#     idx_front = stack_front[i]
#     idx_back = stack_back[i]
#     past_idx_front = stack_front[i-1]
#     past_idx_back = stack_back[i-1]
#
#     temp = input_str[idx_front+1: past_idx_front-1] + cur + input_str[past_idx_back+1: idx_back]
#     cur = temp*int(input_str[idx_front-1])
#
# answer = int(stack_front[-1])-1 + len(cur) + (len(input_str)-int(stack_back[-1])-1)
# print(answer)

### 2. Second Approach
stack = []
for idx, c in enumerate(input_str):
    if c == ")":
        temp = 0
        while stack:
            t = stack.pop()
            if t == "(":
                reply_cnt = int(stack.pop())
                temp = temp*reply_cnt
                stack.append(temp)
                break
            else:
                temp += t
    elif c == "(":
        stack.append(c)
    else:
        if idx+1 < len(input_str) and input_str[idx+1] == "(":
            stack.append(int(c))
        else:
            stack.append(1)

print(sum(stack))

explain = """
첫번째 시도에서는 괄호의 인덱스를 바탕으로 괄호 안의 문자열이 변환되는 것을 기록하며 진행하였다. 
그러나 괄호가 중첩되어 있지 않은 예제에 대해 처리가 안되는 로직이었고 두번째 접근 방법으로 스택에
문자열을 넣어가며 괄호가 완성될때마다 문자열을 합쳐 스택에 넣어주는 로직으로 변환하였다.
문자열을 그대로 스택에 저장시에 메모리 초과가 발생하여 길이에 대한 숫자가 넣어지도록 하였고
이때, 괄호 바로 왼쪽에 있는 숫자와 다른 숫자들에 대해 다르게 처리하는게 로직에서 주요한 부분이었다.
"""