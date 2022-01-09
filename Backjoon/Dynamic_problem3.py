import math

def countN(n):
    module2 = n//2
    module1 = n-2*module2

    result = 0
    final_result = 0
    if module1 == 0:
        init = 1
        result += init
        for i in range(1, module2+1):
            module2-=1
            module1+=2
            init = init * (module1 + module2) * (1 + module2) / (2 * i) / (2 * i - 1)
            if init % 15746 ==0:
                continue
            else:
                result += init
            print(result)
        result =  result % 15746

    elif module1 == 1:
        init = module1 + module2
        result += init
        for i in range(1, module2+1):
            module2-=1
            module1+=2
            init = init * (module1 + module2) * (1 + module2) / (2 * i+1) / (2 * i)
            if init%15746 ==0:
                continue
            else: result += init
        result = result % 15746
    return int(result)




def medthod2(n):
    cri = n//2

    if n%2 == 0:
        init  = 1
        final = 2
        mod1 = 2
        mod2 = cri-1
        dn = mod1+mod2
        dn_2 = dn-1
        dnn = 2
        dnn_2 = dnn-1
        for i in range(1,cri):
            init = init*dn*dn_2/(dnn*dnn_2)
            dn +=1
            dn_2-=1
            dnn+=2
            dnn_2+=2
            final += init%15746
            if dn>= 7873:
                break

        return int(final%15746)

    elif n%2 !=0:
        final = 1
        final += (cri+1)%15746
        init = cri+1
        dn = cri+2
        dn_2 = cri
        dnn = 3
        dnn_2 = 2
        for i in range(1, cri):
            init = init * dn * dn_2 / (dnn * dnn_2)
            dn += 1
            dn_2 -= 1
            dnn += 2
            dnn_2 += 2
            final += init%15746
            print(dn, dnn, init)
            if dn>= 7837 :
                break

        return int(final % 15746)

import sys
def method3(n):

    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        if n<= 100:
            pivo_list = [0] * n
            pivo_list[0] = 1
            pivo_list[1] = 2

            for i in range(2,len(pivo_list)):
                pivo_list[i] = pivo_list[i-1]+pivo_list[i-2]

            return pivo_list[-1]%15746

        else:
            reset_1 = 1
            reset_2 = 2
            for i in range(n//100):
                pivo_list = [0]*100
                pivo_list[0] = (reset_1 + reset_2)%15746
                pivo_list[1] = (pivo_list[0] + reset_2)%15746
                for i in range(2, 100):
                    pivo_list[i] = pivo_list[i - 1] + pivo_list[i - 2]
                reset_1 = pivo_list[-2]
                reset_2 = pivo_list[-1]

            cri = n%100
            pivo_list = [0]*cri
            pivo_list[0] = reset_1 + reset_2
            pivo_list[1] = pivo_list[0] + reset_2
            for i in range(2, cri):
                pivo_list[i] = pivo_list[i-1] + pivo_list[i-2]

            return pivo_list[-1]%15746


import sys
from tqdm import tqdm
length_num = int(sys.stdin.readline())
if length_num == 1:
    print(1)
    sys.exit()
elif length_num == 2:
    print(2)
    sys.exit()
A = [0]*(length_num+1)
A[1] = 1
A[2] = 1

for i in tqdm(range(1, length_num-1)):
    A[i+1] += A[i]%15746
    A[i+2] += A[i]%15746

A[i+2] += A[i+1]
print(A[-1]%15746)

