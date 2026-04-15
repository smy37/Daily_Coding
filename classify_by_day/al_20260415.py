import sys

M = int(sys.stdin.readline())

start_word = {}
end_word = {}
word_list = []

for _ in range(M):
    word = sys.stdin.readline().strip()
    word_list.append(word)

    if word[0] not in start_word:
        start_word[word[0]] = []
    start_word[word[0]].append(word)

    if word[-1] not in end_word:
        end_word[word[-1]] = []
    end_word[word[-1]].append(word)

final_word = {}
for e in end_word:
    if e not in start_word:
        for word in end_word[e]:
            final_word[word[0]] = word

answer_list = []
answer = {}
def dfs(cur_word, cur_idx, visit):
    if cur_word in answer:
        if cur_idx%2 == 0:
            return 0
        else:
            return 1
    if cur_word[-1] not in start_word:
        if cur_idx%2 == 0:
            return 0
        else:
            return 1
    for next_word in start_word[cur_word[-1]]:
        if next_word[0] in final_word:
            if (cur_idx+1)%2 == 0:
                return 0
            else:
                return 1
    record = {}
    for next_word in start_word[cur_word[-1]]:
        if next_word[0] == next_word[-1]:
            return 2
        if next_word not in visit:
            visit[next_word] = True
            r = dfs(next_word, cur_idx+1, visit)
            record[r] = True

    if 0 in record and 1 in record:
        return 2
    elif 0 in record:
        return 0
    elif 1 in record:
        return 1


for word in word_list:
    if word[0] == word[-1]:
        continue
    visit = {}
    flag = dfs(word, 0, visit)
    if flag == 0:
        answer[word] = 1

print(len(answer))
for k in answer:
    print(k)