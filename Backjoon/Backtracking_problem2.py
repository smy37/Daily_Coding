import sys

def Com(A,n):
    result = []
    limit = len(A)
    indices = list(range(n))
    result.append([A[w] for w in indices])
    while True:
        for i in reversed(range(n)):
            if indices[i]!=limit-n+i:
                break
        else:
            return result
        indices[i]+=1
        for j in range(i+1,n):
            indices[j]=indices[j-1]+1
        result.append([A[w] for w in indices])


a, b = map(int, sys.stdin.readline().rstrip().split())
num_list = tuple(w+1 for w in range(a))
A = Com(num_list,b)
for i in A:
    for j in i:
        print(j,end=' ')
    print()
