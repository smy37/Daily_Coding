import sys
import math

ball_r = 10
target_r = 6

T = int(sys.stdin.readline())

for _ in range(T):
    dist, angle = sys.stdin.readline().split()
    dist = float(dist)*100
    angle = int(angle)

    angle_dist = (target_r+ball_r)/(math.sin(math.radians(angle)))
    target_dist = (52.5-ball_r)/(math.tan(math.radians(angle)))

    step = 2*target_dist

    rest = dist % step

    if rest <= angle_dist or (step-rest) <= angle_dist:
        print("yes")
    else:
        print("no")

explain = """
처음에는 주기를 생각못하고 첫번째 바운스 하고 충돌하는 경우만 체크하였었다. 충돌 가능성이 있는 주기는 2*target_dist이고
이 주기에 충돌하는지 체크하기 위해서 rest = dist % step 으로 잔차를 구하였는데 잔차가 주기의 중심점을 넘어서 있는 경우와
못미쳐 있는 경우를 if rest <= angle_dist or (step-rest) <= angle_dist와 같은 조건식으로 모두 체크해줘야 한다.
"""