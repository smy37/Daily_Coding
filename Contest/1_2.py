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
def solution(Braille):
    answer = ""
    p_num_r = {}
    for i in p_num:
        temp = ''
        for j in p_num[i]:
            for k in j:
                temp += str(k)
        p_num_r[temp] = str(i)
    for i in range(len(Braille[0])//2):
        temp = ''
        for j in range(2):
            temp += Braille[j][i*2:(i+1)*2]
        temp += '00'
        answer += p_num_r[temp]
    return answer

print(solution(["01101011", "11001000", "00000000"]))