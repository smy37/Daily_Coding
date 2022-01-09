import sys

n, b = map(int, sys.stdin.readline().rstrip().split())

ml = []
for i in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    ml.append(temp)

for i in range(n):
    for j in range(n):
        ml[i][j] = ml[i][j]%1000

def m_multiply(A,B):
    final = []
    for i in range(len(A)):
        temp = []
        for j in range(len(B)):
            temp_sum = 0
            for k in range(len(A[i])):
                temp_sum += A[i][k]*B[k][j]
            temp.append(temp_sum%1000)
        final.append(temp)

    return final


def m_square(A,b):
    if b == 1:
        return A

    elif b%2 == 0:
        temp = m_square(A, b//2)
        return m_multiply(temp, temp)
    elif b%2 == 1:
        temp = m_square(A, b//2)
        return m_multiply(m_multiply(temp, temp), ml)


result = m_square(ml, b)
for i in result:
    for j in i:
        print(j, end = ' ')
    print()
