import sys

equation = sys.stdin.readline().strip()
split_eq = equation.split("x")
answer = ""

if len(split_eq) >= 2:
    w = int(split_eq[0])
    if w//2 == 1:
        next_w = ""
    elif w //2 == -1:
        next_w = "-"
    else:
        next_w = str(w//2)

    back_eq = split_eq[1]

    if len(back_eq) == 0:
        answer += next_w + "xx" + "+W"
    else:
        if back_eq[1] != "0":
            if back_eq[1] == "1" and len(back_eq) == 2:
                answer += next_w + "xx" + back_eq[0] + "x" + "+W"
            else:
                answer += next_w + "xx" + back_eq + "x" + "+W"
        else:
            answer += next_w + "xx" + "+W"

else:
    c = split_eq[0]

    if c == "0":
        answer = "W"
    else:
        if c == "1":
            answer += "x" + "+W"
        elif c == "-1":
            answer += "-x" + "+W"
        else:
            answer += c+"x" + "+W"

print(answer)

explain = """
문제의 구현도 쉽고 문제 자체도 쉬워서 빠르게 풀 수 있었지만 엣지 케이스의 늪이 깊었던 문제.
적분후 계수가 1 또는 -1이 되는 상황을 생각해야 했고 일차항만 주어지는 경우와 상수항만 주어지는 경우도 생각해야 했다.
또한 상수항으로 0이 주어지는 경우도 엣지 케이스로 발생하였다.
"""