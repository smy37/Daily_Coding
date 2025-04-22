def solution(m, n, puddles):
    pan = []
    for i in range(n):
        pan.append([0]*m)
    pan[0][0] = 1
    for i in range(n):
        for j in range(m):
            if [j+1, i+1] in puddles:
                continue
            else:
                if i+1 < n:
                    pan[i+1][j] += pan[i][j]
                    pan[i+1][j] %= 1000000007
                if j +1 < m:
                    pan[i][j+1] += pan[i][j]
                    pan[i][j+1] %= 1000000007

    answer = pan[n-1][m-1]
    return answer



if __name__ == "__main__":
    m = 2
    n = 2
    puddles = []
    print(solution(2, 2, []), 2)
    print(solution(3, 3, []), 6)
    print(solution(3, 3, [[2, 2]]), 2)
    print(solution(3, 3, [[2, 3]]), 3)
    print(solution(3, 3, [[1, 3]]), 5)
    print(solution(3, 3, [[1, 3], [3, 1]]), 4)
    print(solution(3, 3, [[1, 3], [3, 1], [2, 3]]), 2)
    print(solution(3, 3, [[1, 3], [3, 1], [2, 3], [2, 1]]), 1)
    print(solution(7, 4, [[2, 1], [2, 2], [2, 3], [4, 2], [4, 3], [4, 4], [6, 2], [6, 3]]),0)
    print(solution(4, 4, [[3, 2], [2, 4]]), 7)
    print(solution(100, 100, []), 690285631)
