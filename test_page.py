import sys
import re
from itertools import combinations

N, K = map(int, sys.stdin.readline().split())

ord_set = []
if K < 5:
    print(0)
else:
    word_masks = []
    for _ in range(N):
        word = sys.stdin.readline().strip()
        mask = 0
        for char in set(word) - {'a', 'n', 't', 'i', 'c'}:
            mask |= (1 << (ord(char) - ord('a')))
            ord_set.append(ord(char) - ord('a'))
        word_masks.append(mask)

    answer = 0
    ord_set = set(ord_set)
    if K-5 >= len(ord_set):
        answer = N
    else:
        for comb in combinations(ord_set, K-5):
            comb_mask = 0
            for i in comb:
                comb_mask |= (1 << i)
            temp_ans = sum(1 for word_mask in word_masks if word_mask & comb_mask == word_mask)
            answer = max(answer, temp_ans)

    print(answer)

