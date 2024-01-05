p_num = {}
p_num[0] = [[0,1],[1,1],[0,0]]
p_num[1] = [[1,0],[0,0],[0,0]]
p_num[2] = [[1,0],[1,0],[0,0]]
p_num[3] = [[1,1],[0,0],[0,0]]
p_num[4] = [[1,1],[0,1],[0,0]]
p_num[5] = [[1,0],[0,1],[0,0]]
p_num[6] = [[1,1],[1,0],[0,0]]
p_num[7] = [[1,1],[1,1],[0,0]]
p_num[8] = [[1,0],[1,1],[0,0]]
p_num[9] = [[0,1],[1,0],[0,0]]

p_al = {}
p_al['a'] = [[1,0],[0,0],[0,0]]
p_al['b'] = [[1,0],[1,0],[0,0]]
p_al['c'] = [[1,1],[0,0],[0,0]]
p_al['d'] = [[1,1],[0,1],[0,0]]
p_al['e'] = [[1,0],[0,1],[0,0]]
p_al['f'] = [[1,1],[1,0],[0,0]]
p_al['g'] = [[1,1],[1,1],[0,0]]
p_al['h'] = [[1,0],[1,1],[0,0]]
p_al['i'] = [[0,1],[1,0],[0,0]]
p_al['j'] = [[0,1],[1,1],[0,0]]
p_al['k'] = [[1,0],[0,0],[1,0]]
p_al['l'] = [[1,0],[1,0],[1,0]]
p_al['m'] = [[1,1],[0,0],[1,0]]
p_al['n'] = [[1,1],[0,1],[1,0]]
p_al['o'] = [[1,0],[0,1],[1,0]]
p_al['p'] = [[1,1],[1,0],[1,0]]
p_al['q'] = [[1,1],[1,1],[1,0]]
p_al['r'] = [[1,0],[1,1],[1,0]]
p_al['s'] = [[0,1],[1,0],[1,0]]
p_al['t'] = [[0,1],[1,1],[1,0]]
p_al['u'] = [[1,0],[0,0],[1,1]]
p_al['v'] = [[1,0],[1,0],[1,1]]
p_al['w'] = [[0,1],[1,1],[0,1]]
p_al['x'] = [[1,1],[0,0],[1,1]]
p_al['y'] = [[1,1],[0,1],[1,1]]
p_al['z'] = [[1,0],[0,1],[1,1]]

chkDigit = [[0,1],[0,1],[1,1]]
chkUpper = [[0,0],[0,0],[0,1]]

def solution(Words):
    answer = []

    for i in range(3):
        f_digit = False
        f_upper = False
        temp = ""
        for j in Words:
            if j.isdigit():
                if f_digit == False:
                    if f_upper == True: ##이전 글씨가 대문자일 때...
                        # temp += " "
                        f_upper = False
                    for k in chkDigit[i]:
                        temp += str(k)
                    f_digit = True
                for k in p_num[int(j)][i]:
                    temp += str(k)
                f_digit = True
            else:
                if j.isupper():
                    if f_digit == True:    ## 이전 점자 숫자
                        # temp += " "
                        f_digit = False
                        for k in chkUpper[i]:
                            temp += str(k)
                    elif f_upper == True:  ## 이전 점자 대문자
                        f_upper = True
                    else:   ## 이전 점자 소문자
                        for k in chkUpper[i]:
                            temp += str(k)
                    for k in p_al[j.lower()][i]:
                        temp += str(k)
                    f_upper = True
                else:
                    if f_digit == True:    ## 이전 점자 숫자
                        f_digit = False
                        if j in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']:
                            temp += " "
                    elif f_upper == True:  ## 이전 점자 대문자
                        f_upper = False
                        temp += " "
                    for k in p_al[j][i]:
                       temp += str(k)
        answer.append(temp)
    return answer
