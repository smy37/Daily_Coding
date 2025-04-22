import sys

a,b = map(int, sys.stdin.readline().rstrip().split())
num_list = [w for w in range(1,a+1)]

def selB(A,n):
    num = tuple(A)
    indices = [0]*n
    yield tuple(num[w] for w in indices)
    while True:
        for i in reversed(range(n)):
            if indices[i]!=len(A)-1:
                break
        else:
            return
        indices[i]+=1
        for j in range(i+1,n):
            indices[j]=indices[j-1]
        yield tuple(num[w] for w in indices)

result = selB(num_list,b)
for i in result:
    for j in i:
        print(j,end=' ')
    print()