import sys

answer = 0
N, d, k, c = map(int, sys.stdin.readline().split())

num_list = []
for _ in range(N):
    num_list.append(int(sys.stdin.readline()))

num_list.extend(num_list[:k-1])

memory = {c: 1}

left = 0

for right, n in enumerate(num_list):
    if n not in memory:
        memory[n] = 0
    memory[n] += 1

    if right-left+1 > k:
        memory[num_list[left]] -= 1
        if memory[num_list[left]] == 0:
            del memory[num_list[left]]
        left += 1

    answer = max(answer, len(memory))

print(answer)