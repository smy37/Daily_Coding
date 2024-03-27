import sys
from collections import deque
import copy

N = int(sys.stdin.readline())
g = {}
for i in range(N):
    t = sys.stdin.readline().split()
    g[t[0]] = t[1:]


f_dq = deque()
f_dq.append('A')
f_circuit = ''
while f_dq:
    t = f_dq.popleft()
    f_circuit += t
    for i in [1,0]:
        if g[t][i]!= '.':
            f_dq.appendleft(g[t][i])
print(f_circuit)



m_dq = 'A'
m_circuit = ''
m_g = copy.deepcopy(g)
visited = {}
def mid_circuit(cur_str):
    global m_circuit
    global m_g

    if cur_str not in visited:
        if m_g[cur_str][0] != '.':
            mid_circuit(m_g[cur_str][0])
        m_circuit += cur_str
        visited[cur_str] = 1
        if m_g[cur_str][1] != '.':
            mid_circuit(m_g[cur_str][1])
mid_circuit(m_dq)
print(m_circuit)

b_dq = 'A'
b_circuit = ''
b_g = copy.deepcopy(g)
visited = {}
def back_circuit(cur_str):
    global b_circuit
    global b_g

    if cur_str not in visited:
        if b_g[cur_str][0] != '.':
            back_circuit(b_g[cur_str][0])
        if b_g[cur_str][1] != '.':
            back_circuit(b_g[cur_str][1])
        b_circuit += cur_str
        visited[cur_str] = 1
back_circuit(b_dq)
print(b_circuit)