import sys

a_p = int(sys.stdin.readline())/100
b_p = int(sys.stdin.readline())/100

### 1. First Method, using Dynamic Programming
u_limit = 19
prob_a = [[0 for _ in range(u_limit)] for _ in range(u_limit)]
prob_b = [[0 for _ in range(u_limit)] for _ in range(u_limit)]
prob_a[0][0] = 1
prob_b[0][0] = 1


for n in range(1, u_limit):
    for j in range(n):
        prob_a[n][j] +=  prob_a[n-1][j] * (1-a_p)
        prob_a[n][j+1] += prob_a[n-1][j]*a_p

        prob_b[n][j] +=  prob_b[n-1][j] * (1-b_p)
        prob_b[n][j+1] += prob_b[n-1][j]*b_p

non_prime = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18]
r_a = 0
r_b = 0
for n in non_prime:
    r_a += prob_a[u_limit-1][n]
    r_b += prob_b[u_limit-1][n]

print(1-(r_a*r_b))


### 2. Second Method, Using Math
# import math
# a_t = 0
# b_t = 0
# for n in non_prime:
#     a_t += math.comb(18, n)*(a_p**n)*(1-a_p)**(18-n)
#     b_t += math.comb(18, n)*(b_p**n)*(1-b_p)**(18-n)
#
# print(1-(a_t*b_t))


explain = """
수학의 확률과 경우의 수 성향이 강했던 문제, 굳이 DP가 아니더라도 18번째 섹터의 확률을 공식을 통해서 구할 수 있고 소수가 아닌 경우의 수에 대한 
확률들을 구해준후에 1에서 빼줌으로써도 구할 수 있다. 0도 넣을 수 있는 골의 경우의 수에 들어가기 때문에 0을 prime number에서 빼야한다는 것을 유의해줘야 한다.
"""