import sys

m, n = list(map(int, sys.stdin.readline().split(' ')))

card_list = sorted(map(int,sys.stdin.readline().split(' ')))

temp_max = 0

for i in range(m):
    if card_list[i] >=n :
        break
    for j in range(i+1, m):
        if card_list[j] >= n :
            break
        for k in range(j+1, m):
            if card_list[k] >= n :
                break
            else:
                if card_list[i]+card_list[j]+card_list[k] == n:
                    print(n)
                    sys.exit()
                elif card_list[i]+card_list[j]+card_list[k] < n and temp_max < card_list[i]+card_list[j]+card_list[k]:
                    temp_max = card_list[i]+card_list[j]+card_list[k]

print(temp_max)
