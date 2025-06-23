import sys 

S = sys.stdin.readline().strip()
stack = []


for i in range(len(S)):
    stack.append(S[i])
    
    if len(stack) >= 4 and stack[-4:] == ["P", "P", "A", "P"]:
        for _ in range(3):
            stack.pop()

if stack == ["P"]:
    print("PPAP")
else:
    print("NP")

explain = """
stack에 문자를 추가하면서 특정 문자열이 되면 그 문자열을 치환해준다.
이렇게 해주면 치환된 문자열을 포함해서 특정 문자열이 되는 경우도 카운트 가능해지므로
문자열의 길이가 n일 때, O(n)의 시간복잡도 내에서 해결 가능하다.
"""