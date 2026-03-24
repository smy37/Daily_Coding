import sys

N = int(sys.stdin.readline())
liquids = list(map(int, sys.stdin.readline().split()))
liquids.sort()

answer = float("inf")
left, right = 0, N-1
ans_l, ans_r = liquids[left], liquids[right]

while left < right:
    abs_value = abs(liquids[left]+liquids[right])
    value = liquids[left] + liquids[right]
    if answer > abs_value:
        answer = abs_value
        ans_l, ans_r = liquids[left], liquids[right]

    if value > 0:
        right -=1
    elif value < 0:
        left += 1
    else:
        print(ans_l, ans_r)
        sys.exit()
print(ans_l, ans_r)