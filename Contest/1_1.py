p_num = {}
p_num[0] = [[0,1],[1,1],[0,0]]
p_num[1] = [[0,0],[0,0],[0,0]]
p_num[2] = [[1,0],[1,0],[0,0]]
p_num[3] = [[1,1],[0,0],[0,0]]
p_num[4] = [[1,1],[0,1],[0,0]]
p_num[5] = [[1,0],[0,1],[0,0]]
p_num[6] = [[1,1],[1,0],[0,0]]
p_num[7] = [[1,1],[1,1],[0,0]]
p_num[8] = [[1,0],[1,1],[0,0]]
p_num[9] = [[0,1],[1,0],[0,0]]
def solution(Phone):
    answer = []
    for i in range(3):
        temp =''
        for n in Phone:
            for j in p_num[int(n)][i]:
                temp += str(j)
        answer.append(temp)
    return answer

print(solution("0123"))