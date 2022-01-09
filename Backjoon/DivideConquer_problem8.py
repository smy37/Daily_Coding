import sys

cri = 1000000007

n = int(sys.stdin.readline())

if n == 0 :
    print(0)
    sys.exit()
elif n == 1:
    print(1)
    sys.exit()
temp = [[1,1],[1,0]]

def matcal(A, B):
    return [[(A[0][0]*B[0][0]+A[0][1]*B[1][0])%cri, (A[0][0]*B[0][1] + A[0][1]*B[1][1])%cri], [(A[1][0]*B[0][0]+ A[1][1]*B[1][0])%cri , (A[1][0]*B[0][1] + A[1][1]*B[1][1])%cri]]
n = n-1
def fivona(number):
    if number == 1:
        return temp
    elif number % 2== 0:
        tt = fivona(number//2)

        return matcal(tt,tt)
    elif number %2 == 1:
        tt = fivona((number-1)//2)
        return matcal(matcal(tt,tt), temp)


print(fivona(n)[0][0])



