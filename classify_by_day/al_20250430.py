import sys

x, y, c = map(float, sys.stdin.readline().split())

low = 0
high = min(x,y)

ans = 0
while low + 0.001 <= high:
    mid = (low+high)/2
    a = (x**2-mid**2)**0.5
    b = (y**2-mid**2)**0.5
    cal_c = a*b/(a+b)

    if cal_c >= c:
        ans = mid
        low = mid
    else:
        high = mid

print(ans)

## 직선의 방정식을 2개 구하고 식정리를 수행하여 미지수를 최대한 지우고 c, x, y, d만 남기는 것이 포인트
## d에 대해서 일반화된 식을 구하기 어려우므로 min(x,y)와 0을 바운더리로 두고 이분탐색을 진행한다.
## 이분 탐색의 조건이 헷갈리는데
## if cal_c <= c:
##    ans = mid
##    high = mid  로 하는 조건은 틀리다고 나온다.
## cal_c >=c 일 때만 답이 맞는 이유에 대해 좀더 생각해 봐야 할 듯하다.
##