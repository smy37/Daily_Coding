import sys

N = int(sys.stdin.readline())

word_cnt = {}
for _ in range(N):
    t = sys.stdin.readline().strip()
    t_len = len(t)
    for i in range(len(t)):
        if t[i] not in word_cnt:
            word_cnt[t[i]] = 10**(t_len-i-1)
        else:
            word_cnt[t[i]] += 10**(t_len-i-1)

word_cnt = sorted(word_cnt.items(), key = lambda x : x[1], reverse= True)

answer = 0
cnt = 9

for i in word_cnt:
    answer += cnt*i[1]
    cnt -=1

print(answer)