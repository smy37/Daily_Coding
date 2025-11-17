import sys
sys.setrecursionlimit(10**6)

def union(a, b, parent_dict):
    parent_a = find(a, parent_dict)
    parent_b = find(b, parent_dict)

    if a <= b:
        parent_dict[parent_b] = parent_a
    else:
        parent_dict[parent_a] = parent_b

def find(cur: int, parent_dict: dict):
    parent = parent_dict[cur]
    if cur != parent:
        parent = find(parent, parent_dict)
    return parent

T = int(sys.stdin.readline())

for number in range(T):
    user_num = int(sys.stdin.readline())
    relation_num = int(sys.stdin.readline())
    parent_d = {i: i for i in range(user_num)}
    for i in range(relation_num):
        s, t = map(int, sys.stdin.readline().split())
        union(s, t, parent_d)

    print(f"Scenario {number+1}:")
    q_num = int(sys.stdin.readline())
    for _ in range(q_num):
        a, b = map(int, sys.stdin.readline().split())
        p_a, p_b = find(a, parent_d), find(b, parent_d)

        if p_a == p_b:
            print(1)
        else:
            print(0)
    print()