import sys

T = int(sys.stdin.readline())
n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    n_list[i] += n_list[i-1]
for i in range(1, m):
    m_list[i] += m_list[i-1]

n_dict = {}
m_dict = {}
for i in range(n):
    for j in range(i, n):
        if i == 0:
            cur_num = n_list[j]
        else:
            cur_num = n_list[j]-n_list[i-1]

        if cur_num not in n_dict:
            n_dict[cur_num] = 0
        n_dict[cur_num] +=1

for i in range(m):
    for j in range(i, m):
        if i == 0:
            cur_num = m_list[j]
        else:
            cur_num = m_list[j] - m_list[i - 1]

        if cur_num not in m_dict:
            m_dict[cur_num] = 0
        m_dict[cur_num] += 1

answer = 0
for i in n_dict:
    if T-i in m_dict:
        answer += n_dict[i]*m_dict[T-i]
print(answer)

explain= """
누적합을 이용해서 각 구간의 합을 빠르게 구할수 있도록 한 다음에 각 구간에서 나오는 값을 key로 하고 그 개수를 value 하는 
hash를 2개 구성한다. 첫번째 해시의 key와 T에서 그 key를 빼준 값이 두번째 해시의 key에 있다면 각각의 value를 곱한값을
정답에 더해준다.
"""