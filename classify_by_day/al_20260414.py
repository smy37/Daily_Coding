import sys

N = int(sys.stdin.readline())

matrix = []
for _ in range(N):
    row = sys.stdin.readline().strip()
    matrix.append(row)


stack = []
memory = {(0,0,""): 0}

global answer
answer = 0
def dfs(cur_idx: int, past_value:int , record: list):
    global answer
    if len(record) == N:
        return
    sorted_record = sorted(record + [str(cur_idx)])
    for next_idx in range(len(matrix[cur_idx])):
        if next_idx != cur_idx:
            if int(matrix[cur_idx][next_idx]) >= past_value and str(next_idx) not in record:
                hash_key = tuple([next_idx, int(matrix[cur_idx][next_idx]), "".join(sorted_record)])
                if hash_key not in memory:
                    dfs(next_idx, int(matrix[cur_idx][next_idx]), sorted_record)
                else:
                    continue

    hash_key = tuple([cur_idx, past_value, "".join(record)])
    memory[hash_key] = len(record)+1
    answer = max(answer, len(record)+1)
    return

dfs(0, 0, [])

print(answer)

explain = """When using memoization in dynamic programming, all factors that affect the next step 
(or the number of possible cases) must be included in the state, 
so that different states are treated as distinct cases. """