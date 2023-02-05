def operation(num1, oper, num2):
    if oper == '+':
        return int(num1) + int(num2)
    elif oper == '-':
        return int(num1) - int(num2)

record = {}
def recur(array):
    if len(array) == 3:         ## Case1에서의 끝단계
        return operation(array[0], array[1], array[2])
    else:
        length = len(array)//2
        score = []
        for i in range(length):
            temp_list = []
            k = 2*i
            if i == 0:
                temp_list = [str(operation(array[k],array[k+1], array[k+2]))] + array[k+3:]
            elif i == length -1:
                temp_list = array[:k]+[str(operation(array[k], array[k + 1], array[k + 2]))]
            else:
                temp_list = array[:k] + [str(operation(array[k], array[k + 1], array[k + 2]))] + array[k+3:]
            if tuple(temp_list) not in record:
                t_score = recur(temp_list)
                record[tuple(temp_list)] = t_score
                score.append(t_score)
            else:
                score.append(record[tuple(temp_list)])
        return max(score)

def solution(array):
    answer = 0
    answer = recur(array)
    return answer


if __name__ == '__main__':
    print(solution(["1","-","3","+","5","-","8"]), 1)
    print(solution( ["5", "-", "10", "+", "1", "+", "2", "-", "4"]), -4)

