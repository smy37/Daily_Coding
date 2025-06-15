import sys 

def cal_area(x1, y1, x2, y2, x3, y3):
    S = abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2
    return S

x_1, y_1 = map(int, sys.stdin.readline().split())
x_2, y_2 = map(int, sys.stdin.readline().split())
x_3, y_3 = map(int, sys.stdin.readline().split())

N = int(sys.stdin.readline())

S = cal_area(x_1, y_1, x_2, y_2, x_3, y_3)

cnt = 0
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())

    s1 = cal_area(x, y, x_1, y_1, x_2, y_2)
    s2 = cal_area(x, y, x_2, y_2, x_3, y_3)
    s3 = cal_area(x, y, x_3, y_3, x_1, y_1)

    if abs(S-(s1+s2+s3)) < 1e-7:
        cnt += 1

print(S)
print(cnt)

explain = """
신발끈 공식을 통해서 삼각형의 넓이를 구하는 공식이 제공되었고 이를 이용하였다. 
주어지는 점 P와 나머지 삼각형들의 꼭지점을 이어 3가지 삼각형을 구했을 때, 삼각형의 넓이의 합이 
원래 주어지는 삼각형의 넓이와 같다면 점 P가 내부에 있는 것이고 더 크다면 점 외부에 있는 것이다. 
이에 대한 증명은 도시해 보면 쉽게 증명할 수 있다. 
이외에도 외적을 통해서 삼각형 내-외부의 점인지 판단할 수 있다.
"""