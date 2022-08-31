test = "(()("

def solution(arr):
    answer = []
    final = True
    for i in arr:
        if i == '(':
            answer.append(i)
        elif i == ')':
            try:
                answer.pop()
            except:
                final = False
                break

    if len(answer) !=0:
        final = False
    print(final)
    return final

solution(test)