test = [4,4,4,3,3]


def solution(arr):
    answer = []
    temp = arr[0]
    answer.append(temp)
    for i in range(1,len(arr)):
        if arr[i] != temp:
            answer.append(arr[i])
            temp = arr[i]
        else:
            continue
    print(answer)
    return answer

solution(test)