import sys

equation = sys.stdin.readline().strip()

sign_candidate= ["+", "-", "*", "/"]

### 1. 처음 시도한 방법... *와 / 연산자에 *를 추가한 후에 괄호 안의 연산자를 수행 후 합치는 방법....

# ### *와 / 연산자에 대해서 괄호로 묶어 주기.
#
# total_sign = 0
# for i in range(len(equation)):
#     if equation[i] in ["*", "/"]:
#         total_sign += 1
#
# cur_target_idx = 1
#
# while cur_target_idx <= total_sign:
#     temp = []
#     idx = -1
#     for i in range(len(equation)):
#         if equation[i] in ["*", "/"]:
#             temp.append(i)
#         if len(temp) == cur_target_idx:
#             idx = i
#             cur_target_idx += 1
#             break
#
#
#     ### 전위 탐색
#     if equation[idx-1].isalpha():
#         pre_equation = equation[:idx-1] + "(" + equation[idx-1]
#     else:
#         pt_s = []
#         for j in range(idx-1, -1, -1):
#             if equation[j] == ")":
#                 pt_s.append(")")
#             elif equation[j] == "(":
#                 if len(pt_s) == 0:
#                     break
#                 pt_s.pop()
#             elif equation[j] in sign_candidate and len(pt_s) == 0:
#                 break
#         if j == 0:
#             pre_equation = "(" + equation[:idx]
#         else:
#             pre_equation = equation[:j+1] + "(" + equation[j+1: idx]
#     ### 후위 탐색
#     if equation[idx + 1].isalpha():
#         post_equation = equation[idx: idx +2] + ")" + equation[idx+2:]
#     else:
#         pt_s = []
#         for j in range(idx + 1, len(equation)):
#             if equation[j] == "(":
#                 pt_s.append("(")
#             elif equation[j] == ")":
#                 if len(pt_s) == 0:
#                     break
#                 pt_s.pop()
#             elif equation[j] in sign_candidate and len(pt_s) == 0:
#                 break
#         if j == len(equation)-1:
#             post_equation =equation[idx:] + ")"
#         else:
#             post_equation = equation[idx:j] + ")" + equation[j:]
#
#     equation = pre_equation + post_equation
#
#
# pt_l = []
# symbol_l = []
# sign_l = []
# cur_sym = []
# for i in range(len(equation)):
#     if equation[i] == "(":
#         pt_l.append("(")
#         cur_sym.append(0)
#     elif equation[i] == ")":
#
#         if cur_sym[-1] < 2:
#             acc = cur_sym.pop()
#             if len(cur_sym) > 0:
#                 cur_sym[-1] += acc
#             continue
#         pt_l.pop()
#         post = symbol_l.pop()
#         pre = symbol_l.pop()
#         sign = sign_l.pop()
#         concat_symbol = pre+post+sign
#         symbol_l.append(concat_symbol)
#
#         cur_sym.pop()
#         if len(cur_sym) > 0:
#             cur_sym[-1]+=1
#     elif equation[i] in sign_candidate:
#         sign_l.append(equation[i])
#     else:
#         symbol_l.append(equation[i])
#         if len(cur_sym) >0:
#             cur_sym[-1] += 1
#
#
# if len(sign_l) == 0:
#     print(symbol_l[0])
# else:
#     pre = symbol_l[0]
#     for i in range(len(sign_l)):
#         pre = pre + symbol_l[i+1]+sign_l[i]
#     print(pre)



### 2. 다른 사람의 풀이를 참조한 방법.. 표기법의 성질에 대한 고찰이 필요하다.... output에는 문자... stack에는 괄호와 연산자....

order = {"+":1, "-": 1, "*": 2, "/": 2}

stack = []
output = []
for i in range(len(equation)):
    if equation[i].isalpha():
        output.append(equation[i])
    elif equation[i] == "(":
        stack.append("(")
    elif equation[i] == ")":
        while stack and stack[-1] != "(":
            output.append(stack.pop())
        if stack and stack[-1] == "(":
            stack.pop()
    else:
        while stack and stack[-1] != "(" and order[equation[i]] <= order[stack[-1]]:
            output.append(stack.pop())
        stack.append(equation[i])
while stack:
    output.append(stack.pop())
print(''.join(output))

