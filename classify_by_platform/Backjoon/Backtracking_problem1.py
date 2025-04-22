import sys

def Per(A,n):
    result = []
    length = len(A)
    indices = list(range(length))
    cycles = list(range(length,length-n,-1))
    result.append([A[w] for w in indices[:n]])
    while True:
        for i in reversed(range(n)):
            cycles[i]-=1
            if cycles[i]==0:
                indices[i:] = indices[i+1:]+indices[i:i+1]
                cycles[i] = length - i
            else:
                j = cycles[i]
                indices[i],indices[-j]=indices[-j],indices[i]
                result.append([A[w] for w in indices[:n]])
                break
        else:
            return result


a,b = map(int, sys.stdin.readline().rstrip().split())

num_list = tuple(w+1 for w in range(a))

B = Per(num_list,b)
for i in B:
    for j in i:
        print(j, end=' ')
    print()