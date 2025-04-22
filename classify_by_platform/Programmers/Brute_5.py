import itertools as it

def solution(k, dungeons):
    answer = -1
    l = len(dungeons)
    p = it.permutations(range(l))

    for i in p:
        n_k = k
        cnt = 0
        for idx in i:
            if n_k >= dungeons[idx][0]:
                cnt += 1
                n_k -= dungeons[idx][1]
        answer = max(answer, cnt)

    return answer




if __name__ == "__main__":
    dg = [[80,20],[50,40],[30,10]]
    k = 80
    print(solution(k, dg))