import sys 

T = int(sys.stdin.readline())
for _ in range(T):
    answer = 0
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline())
    for _ in range(n):
        cur_x, cur_y, r = map(int, sys.stdin.readline().split())
        d1 = (x1-cur_x)**2 + (y1-cur_y)**2
        d2 = (x2-cur_x)**2 + (y2-cur_y)**2

        if d1 <= r**2 and d2 > r**2:
            answer += 1
        elif d1 > r**2 and d2 <= r**2:
            answer += 1
        
    print(answer)

explain = """
양 끝점과 원의 중심과의 거리를 구해서 원이 양 끝점을 포함하는지 판단한다.
원이 두 점을 모두 포함하지 않으면서 한점만 포함한다면 궤도상 통과해야 하는
원이 된다.
"""