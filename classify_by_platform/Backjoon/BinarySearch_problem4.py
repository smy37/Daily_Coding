import sys


tree, want = map(int, sys.stdin.readline().rstrip().split(' '))
tree_list = list(map(int, sys.stdin.readline().strip().split(' ')))

def cut_tree(n,treelist):
    temp = 0
    for i in treelist:
        if i>n:
            temp+= (i-n)
    return temp

def binary(cri, start, end):
    if end - start <= 1:
        if cut_tree(end, tree_list) >= cri:
            return end
        else:
            return start

    else:
        mid = (end+start)//2
        temp = cut_tree(mid, tree_list)
        if temp >= cri:
            return binary(cri, mid, end)
        else:
            return binary(cri, start, mid-1)

start = 0
end = max(tree_list)-1

print(binary(want, start, end))