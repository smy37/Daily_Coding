import sys

length = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().strip().split(' ')))

def binary(cur, temp_i):
    start = 0
    end = len(cur)

    answer = -1
    while start <= end:
        mid = (start + end) // 2
        if cur[mid] >= temp_i:
            answer = mid
            end = mid-1
        elif cur[mid] < temp_i:
            start = mid+1

    cur[answer] = temp_i

    return cur

st = [0]

for i in num_list:
    if st[-1] < i :
        st.append(i)
    else:
        st = binary(st, i)

print(len(st)-1)