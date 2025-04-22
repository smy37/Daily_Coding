import sys

input_str = sys.stdin.readline()

answer = 0
length = len(input_str)

def fail_func(string):
    table = [0]*len(string)
    j = 0
    for i in range(1, len(string)):
        while j > 0 and string[i] != string[j]:
            j = table[j-1]
        if string[i] == string[j]:
            j += 1
            table[i] = j
    return max(table)

for i in range(length):
    answer = max(answer, fail_func(input_str[i:length]))

print(answer)