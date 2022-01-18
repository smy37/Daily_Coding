import sys

iter_num = int(sys.stdin.readline())

word_list = []
for i in range(iter_num):
    word_list.append(sys.stdin.readline().strip())


for i in sorted(set(word_list), key = lambda x : [len(x),x]):
    print(i)