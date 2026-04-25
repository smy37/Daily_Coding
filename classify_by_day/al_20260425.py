import sys
from collections import deque

def ccw(x1, y1, x2, y2, x3, y3):
    v1 = [x1-x2, y1-y2]
    v2 = [x1-x3, y1-y3]

    return v1[0]*v2[1]-v1[1]*v2[0]

def cross_check(s1_x, s1_y, e1_x, e1_y, s2_x, s2_y, e2_x, e2_y):
    val_1 = ccw(s1_x, s1_y, e1_x, e1_y, s2_x, s2_y)
    val_2 = ccw(s1_x, s1_y, e1_x, e1_y, e2_x, e2_y)
    val_3 = ccw(s2_x, s2_y, e2_x, e2_y, s1_x, s1_y)
    val_4 = ccw(s2_x, s2_y, e2_x, e2_y, e1_x, e1_y)

    return val_1, val_2, val_3, val_4

m, n = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())

cord_list = {}
for _ in range(k):
    bus_id, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    cord_list[bus_id] = (x1, y1, x2, y2)

s_x, s_y, e_x, e_y = map(int, sys.stdin.readline().split())

start_list = []
end_list = set()
for b_id in cord_list:
    x1, y1, x2, y2 = cord_list[b_id]

    if min(x1, x2) <= s_x <= max(x1, x2) and min(y1, y2) <= s_y <= max(y1, y2):
        start_list.append(b_id)

    if min(x1, x2) <= e_x <= max(x1, x2) and min(y1, y2) <= e_y <= max(y1, y2):
        end_list.add(b_id)

def check_connect(x1, y1, x2, y2, x3, y3, x4, y4):
    cv1, cv2, cv3, cv4 = cross_check(x1, y1, x2, y2, x3, y3, x4, y4)
    if cv1 * cv2 <= 0 and cv3 * cv4 <= 0:
        if cv1 == 0 and cv2 == 0 and cv3 == 0 and cv4 == 0:
            if max(x1, x2) < min(x3, x4) or min(x1, x2) > max(x3, x4) or max(y1, y2) < min(y3, y4) or min(y1, y2) > max(
                    y3, y4):
                return False
        return True
    return False

## First Approach
# graph = {}
# node_id = list(cord_list.keys())
# for i in range(len(node_id)):
#     x1, y1, x2, y2 = cord_list[node_id[i]]
#     for j in range(i+1, len(node_id)):
#         x3, y3, x4, y4 = cord_list[node_id[j]]
#
#         cv1, cv2, cv3, cv4 = cross_check(x1, y1, x2, y2, x3, y3, x4, y4)
#         if cv1*cv2 <=0 and cv3*cv4 <= 0:
#             if cv1 == 0 and cv2 == 0 and cv3 == 0 and cv4 == 0:
#                 if max(x1, x2) < min(x3, x4) or min(x1, x2) > max(x3, x4) or max(y1, y2) < min(y3, y4) or min(y1, y2) > max(y3, y4):
#                     continue
#             if node_id[i] not in graph:
#                 graph[node_id[i]] = {}
#
#             if node_id[j] not in graph:
#                 graph[node_id[j]] = {}
#
#             graph[node_id[i]][node_id[j]] = True
#             graph[node_id[j]][node_id[i]] = True


answer = float("inf")

dq = deque()
visit = {}
for s_id in start_list:
    dq.append((s_id, 1))
    visit[s_id] = True

while dq:
    cur_id, cnt = dq.popleft()
    if cur_id in end_list:
        answer= min(answer, cnt)
        break
    for next_id in cord_list:
        if next_id not in visit:
            x1, y1, x2, y2 = cord_list[cur_id]
            x3, y3, x4, y4 = cord_list[next_id]
            if check_connect(x1, y1, x2, y2, x3, y3, x4, y4):
                visit[next_id] = True
                dq.append([next_id, cnt + 1])

print(answer)

explain = """Instead of checking connectivity between all pairs of nodes in O(n²) time 
and constructing the full edge graph in advance, 
we can perform BFS from selected starting points.

By doing so, we only check connectivity for reachable nodes, 
which avoids building the entire graph and is more memory-efficient.  
In practice, this often requires checking far fewer than O(n²) pairs.
"""