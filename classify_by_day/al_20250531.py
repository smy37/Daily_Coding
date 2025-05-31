import sys
import math
K = int(sys.stdin.readline())

### 1. First Method
# cri = int(math.log2((K/2+1)))
# pre_sum = 2*(2**cri-1)
# next_num = K-pre_sum
# if next_num == 0:
#     print(int("7"*cri))
# else:
#     next_num -=1
#     temp= []
#     while next_num > 1:
#         temp.append(next_num%2)
#         next_num = next_num//2
#     if next_num == 1:
#         temp.append(1)
#
#     for i in range((cri+1)-len(temp)):
#         temp.append(0)
#     answer = ""
#     for num in temp:
#         if num == 0:
#             answer = "4" + answer
#         elif num == 1:
#             answer = "7" + answer
#     print(int(answer))

### 2. Second Method
length = 1
while K > 2**length:
    K -= 2**length
    length +=1

K -=1
binary_k = bin(K)[2:].zfill(length)
answer = "".join("4" if c == "0" else "7" for c in binary_k)
print(int(answer))


explain= """
첫번째 방법과 두번재 방법 모두 답을 구하는 정해이다. 그러나, 두번째 방법은 bin과 zfill 함수를 이용하여 더 보기 쉽게 
답을 구하는 것이 가능하다. 또한, 등비수열의 합으로 현재 구하려는 수의 길이에서 몇번째 수인지 구하는 단계를 두번째 방법에서
while 문을 써서 더 알아보기 쉽게 구하였다. 그러나 두 방법 모두, K-=1을 해줘서 0번부터 세줘야 하는 것은 변하지 않는다.
"""