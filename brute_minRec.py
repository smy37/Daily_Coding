test = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]


def solution(sizes):
    answer = 0
    t_x, t_y = 0, 0
    for i in sizes:
        if t_x < min(i):
            t_x = min(i)
        if t_y < max(i):
            t_y = max(i)

    answer = t_x*t_y
    print(answer)

    return answer

solution(test)