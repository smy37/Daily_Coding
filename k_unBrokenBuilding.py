def solution(board, skill):
    answer = 0
    temp = []
    for i in range(len(board)):
        t = [0] * len(board[i])
        temp.append(t)

    for sk in skill:
        if sk[0] == 1:
            temp[sk[1]][sk[2]] += -sk[5]
            if sk[4]+1 < len(board[0]) and sk[3]+1 < len(board):
                temp[sk[3]+1][sk[4]+1] += -sk[5]
            if sk[4]+1 < len(board[0]):
                temp[sk[1]][sk[4]+1] += sk[5]
            if sk[3]+1 < len(board):
                temp[sk[3]+1][sk[2]] += sk[5]

        elif sk[0] == 2:
            temp[sk[1]][sk[2]] += sk[5]
            if sk[4]+1 < len(board[0]) and sk[3]+1 < len(board):
                temp[sk[3]+1][sk[4]+1] += sk[5]
            if sk[4]+1 < len(board[0]):
                temp[sk[1]][sk[4]+1] += -sk[5]
            if sk[3]+1 < len(board):
                temp[sk[3]+1][sk[2]] += -sk[5]
    for row in range(len(temp)):
        for col in range(1, len(temp[row])):
            temp[row][col] += temp[row][col - 1]

    for row in range(len(temp) - 1):
        for col in range(len(temp[row])):
            temp[row + 1][col] += temp[row][col]
            if temp[row + 1][col] + board[row + 1][col] > 0:
                answer += 1

    for col in range(len(temp[0])):
        if temp[0][col] + board[0][col] > 0:
            answer += 1
    return answer

if __name__ == "__main__":
    print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]),10)