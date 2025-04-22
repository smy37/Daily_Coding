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
visited = {}
def mid_circuit(cur_str):
    global m_circuit
    global g

    if g[cur_str][0] != '.':
        mid_circuit(g[cur_str][0])
    m_circuit += cur_str
    if g[cur_str][1] != '.':
        mid_circuit(g[cur_str][1])
mid_circuit(m_dq)
print(m_circuit)

b_dq = 'A'
b_circuit = ''

def back_circuit(cur_str):
    global b_circuit
    global g

    if g[cur_str][0] != '.':
        back_circuit(g[cur_str][0])
    if g[cur_str][1] != '.':
        back_circuit(g[cur_str][1])
    b_circuit += cur_str
    visited[cur_str] = 1

back_circuit(b_dq)

print(b_circuit)