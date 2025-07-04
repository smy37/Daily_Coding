import sys


answer = 0

def dfs(cur, target):
    global answer
    if len(target) == len(cur):
        if cur == target:
            answer =1
        return

    if cur[0] == "B":
        new_str = cur[-1:0:-1]
        dfs(new_str, target)
    if cur[-1] == "A":
        new_str = cur[0:-1]
        dfs(new_str, target)

S = sys.stdin.readline().strip()
T = sys.stdin.readline().strip()

dfs(T, S)
print(answer)

explain = """
처음에는 짧은 글자에서 긴글자를 만들려고 하였다. 그러나 짧은 글자에서 긴 글자를 만들때는
무조건 2^n 만큼 경우의 수가 생긴다. 그러나 긴글자에서 짧은 글자를 만들 때는, 맨 앞의 문자와
뒤의 문자를 체크함으로써, 경우의 수가 줄어드는 경우가 발생하므로 훨씬 더 빠르게 처리할 수 있다.
"""