import sys
sys.setrecursionlimit(10**8)
N = int(sys.stdin.readline())
in_order = list(map(int, sys.stdin.readline().split()))
post_order = list(map(int, sys.stdin.readline().split()))

in_value = {in_order[i]: i for i in range(N)}
def make_tree(in_s, in_e, post_s, post_e):
    if in_s > in_e or post_s > post_e:
        return

    root = post_order[post_e]
    root_idx = in_value[root]

    left_n = root_idx - in_s

    print(root, end=' ')
    make_tree(in_s, in_s+left_n-1, post_s, post_s+left_n-1)
    make_tree(in_s+left_n+1, in_e, post_s+left_n, post_e-1)

make_tree(0, N-1, 0, N-1)