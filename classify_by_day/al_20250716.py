import sys

input_str = sys.stdin.readline().strip()
stack = []
for s in input_str:
    if s == "(":
        stack.append(s)
    elif s == "[":
        stack.append(s)
    elif s == ")":
        temp = 0
        while stack and stack[-1] != "(":
            t = stack.pop()
            if not isinstance(t, int):
                print(0)
                sys.exit()
            temp += t
        if stack and stack[-1] == "(":
            stack.pop()
        else:
            print(0)
            sys.exit()
        if temp == 0:
            stack.append(2)
        else:
            stack.append(2*temp)
    elif s == "]":
        temp = 0
        while stack and stack[-1] != "[":
            t = stack.pop()
            if not isinstance(t, int):
                print(0)
                sys.exit()
            temp += t
        if stack and stack[-1] == "[":
            stack.pop()
        else:
            print(0)
            sys.exit()
        if temp == 0:
            stack.append(3)
        else:
            stack.append(3*temp)

if any(not isinstance(x, int) for x in stack):
    print(0)
    sys.exit()

print(sum(stack))

explain = """
첫 시도에서는 괄호들마 스택에서 처리하고 수들을 따로 처리하는 방식을 시도하였다. 
그러나 덧셈에 대한 처리와 곱셈에 대한 처리가 쉽지 않아 수들도 스택에 넣고 while 문을 이용하여
괄호가 닫힐 때마다 기록되던 수들을 더해주고 곱셈을 해주는 방식으로 해결하였다.
"""