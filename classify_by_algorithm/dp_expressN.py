import copy
import math
def solution(N, number):
    answer = 0
    NumToCnt = {}
    CntToNum = {}
    NumToCnt[N] = 1
    for i in range(1, 9):
        CntToNum[i] = []
    CntToNum[1].append(N)

    for i in range(2, 9):
        for x in range(math.ceil(i/2)):
            end = x+1
            st = i - end
            st_list = CntToNum[st]
            end_list = CntToNum[end]

            for a in st_list:
                for b in end_list:
                    for k in range(4):
                        if k == 0:
                            if a+b not in NumToCnt:
                                NumToCnt[a+b] = i
                                CntToNum[i].append(a+b)
                            elif a+b in NumToCnt and NumToCnt[a+b] > i :
                                CntToNum[NumToCnt[a + b]].remove(a+b)
                                NumToCnt[a+b] = i
                        elif k == 1:
                            if a-b > 0:
                                if a- b not in NumToCnt:
                                    NumToCnt[a-b] = i
                                    CntToNum[i].append(a-b)
                                elif a - b in NumToCnt and NumToCnt[a - b] > i:
                                    CntToNum[NumToCnt[a - b]].remove(a - b)
                                    NumToCnt[a - b] = i
                        elif k == 2:
                            if a*b not in NumToCnt:
                                NumToCnt[a*b] = i
                                CntToNum[i].append(a*b)
                            elif a * b in NumToCnt and NumToCnt[a * b] > i:
                                CntToNum[NumToCnt[a * b]].remove(a * b)
                                NumToCnt[a * b] = i
                        elif k == 3:
                            if a//b > 0:
                                if a//b not in NumToCnt:
                                    NumToCnt[a//b] = i
                                    CntToNum[i].append(a//b)
                                elif a // b in NumToCnt and NumToCnt[a // b] > i:
                                    CntToNum[NumToCnt[a // b]].remove(a // b)
                                    NumToCnt[a // b] = i

        temp_num = int(str(N)*i)
        if temp_num not in NumToCnt:
            NumToCnt[temp_num] = i
            CntToNum[i].append(temp_num)
    if number in NumToCnt:
        answer = NumToCnt[number]
    else:
        answer = -1
    return answer



if __name__ == "__main__":
    N = 5
    number = 31168
    print(solution(N, number))


