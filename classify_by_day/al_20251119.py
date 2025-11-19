import sys
from itertools import permutations

### 1. First Approach
# N = int(sys.stdin.readline())
# word_dict = {}
# for _ in range(N):
#     word = sys.stdin.readline().strip()
#     word_dict[word] = True
#
# M = int(sys.stdin.readline())
# for _ in range(M):
#     sentence = sys.stdin.readline()
#     sentence_word = sentence.split()
#
#     answer = 1
#     for word in sentence_word:
#
#         temp = 0
#         parsed = word[1:-1]
#         temp_dict = {}
#         for iter in permutations(parsed):
#             check = word[0]+"".join(iter)+word[-1]
#             if check in word_dict and check not in temp_dict:
#                 temp +=1
#                 temp_dict[check] = True
#         if temp == 0:
#             temp = 1
#         answer *= temp
#
#     print(answer)


### 2. Second Approach
N = int(sys.stdin.readline())
word_dict = {}
for _ in range(N):
    word = sys.stdin.readline().strip()
    word_key = word[0]+word[-1]+"".join(sorted(word[1:-1])) if len(word) >1 else word
    if word_key not in word_dict:
        word_dict[word_key] = 0
    word_dict[word_key] += 1

M = int(sys.stdin.readline())
for _ in range(M):
    answer = 1
    flag = False

    sentence = sys.stdin.readline()
    for word in sentence.split():
        word_key = word[0]+word[-1]+"".join(sorted(word[1:-1])) if len(word) > 1 else word
        if word_key in word_dict:
            flag = True
            answer *= word_dict[word_key]


    if not flag:
        print(0)
    else:
        print(answer)

explain = """
처음 시도에서는 가운데 문자열을 순열로 모든 경우를 체크하였고 시간초과가 발생하였다. 
두번째 접근에서는 맨앞뒤 문자열을 고정하고 중간 문자열을 정렬한 것으로 문자열 키를 구성하고 
문자열 키가 동일한 사전의 단어의 개수를 기록해두어 문장에서 만들어지는 문자열 키로 최종 답을 구해준다.
"""