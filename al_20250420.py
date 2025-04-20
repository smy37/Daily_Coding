import sys

### Method 1. B의 범위를 (A**2-1)/2 를 통해서 구함.
# while 1:
#     A = int(sys.stdin.readline())
#     if A == 0:
#         break
#     b_max = int((A**2-1)/2)
#     b_min = A+1
#     answer = 0
#     for i in range(b_min, b_max+1):
#         cri = math.sqrt(A**2+i**2)
#         if cri%1 == 0:
#             answer += 1
#
#     print(answer)

### Method 2. B-C의 범위를 1<= B-C <= A-1로 한정

while 1:
    A = int(sys.stdin.readline())
    if A == 0:
        break
    answer = 0
    for i in range(1, A):
        B = (A**2-i**2)/i/2 ## 해당 수는 i가 커질수록 값이 작아짐로 아래의 break 시행이 가능해진다!!
        if B < A:
            break
        if B%1 == 0:
            answer +=1
    print(answer)