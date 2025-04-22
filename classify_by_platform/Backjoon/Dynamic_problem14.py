import sys


line_1 = sys.stdin.readline().strip()
line_2 = sys.stdin.readline().strip()


if len(line_1) == 0 or len(line_2) == 0:
    print(0)
    sys.exit()
elif len(line_1) == 1:
    if line_1 in line_2:
        print(1)
        sys.exit()
    else:
        print(0)
        sys.exit()
elif len(line_2) == 1:
    if line_2 in line_1:
        print(1)
        sys.exit()
    else:
        print(0)
        sys.exit()

A = []
for i in range(len(line_2)+1):
    temp  = []
    for j in range(len(line_1)+1):
        temp.append(0)
    A.append(temp)



for i in range(1, len(line_2)+1):
    for j in range(1, len(line_1)+1):
        if line_2[i-1] == line_1[j-1]:
            A[i][j] = A[i-1][j-1]+1
        else:
            A[i][j] = max(A[i-1][j], A[i][j-1])

a = len(line_1)
b = len(line_2)

print(max(A[b][a], max(A[b-1][a], A[b][a-1])))