test = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]


def solution(routes):
    answer = 0
    in_list = {}
    out_list = {}
    routes = sorted(routes, key = lambda x : x[0])

    start = routes[0]
    t_cri = start[1]
    answer = 1
    for i in range(1, len(routes)):
        if t_cri >= routes[i][0]:
            t_cri = min(t_cri, routes[i][1])
        else:

            answer += 1
            t_cri = routes[i][1]
    print(answer)
    return answer


solution(test)