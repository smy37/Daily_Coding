import sys

nk_num = list(map(int, sys.stdin.readline().split()))
n, k = nk_num[0], nk_num[1]
nk_num = [i for i in range(1, n+1)]
result = []
temp_result = []

temp_result.append(nk_num[k-1])
if n == 1:
    print('<1>')
    sys.exit()
if k == 1:
    print('<', end ='')
    for i in range(1, n):
        print(i, end = ', ')
    print(f'{n}', end = '>')
    sys.exit()
temp = k-1
cri = n
while len(nk_num) >2 :
    if temp + k <= len(nk_num)-1:
        temp = temp + k
        temp_result.append(nk_num[temp])
    else:
        result = result + temp_result
        for i in temp_result:
            nk_num.remove(i)
        temp = k - (cri-1-temp) - 1
        temp = temp%k
        temp_result = []
        if len(nk_num) == 2:
            break
        if temp !=0:
            temp = temp % len(nk_num)

        temp_result.append(nk_num[temp])
        cri = len(nk_num)

if temp % 2== 0:
    result.append(nk_num[0])
    result.append(nk_num[1])
else:
    result.append(nk_num[1])
    result.append(nk_num[0])

print('<', end = '')
for i in result[:-1]:
    print(i, end = ', ')
print(result[-1], end = '>')