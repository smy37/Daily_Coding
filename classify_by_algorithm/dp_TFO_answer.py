def solution(array):
    answer = 0
    inf = 999999999999
    max_dp = []
    min_dp = []
    length = len(array)//2+1
    for i in range(length):
        max_dp.append([-inf]*length)
        min_dp.append([inf]*length)

    for step in range(length):
        for i in range(length-step):
            c_i = 2*i
            if step == 0:
                max_dp[i][i] = int(array[c_i])
                min_dp[i][i] = int(array[c_i])
            else:
                for j in range(i, i+step):
                    c_j = 2*j
                    if array[c_j+1] == '+':
                        max_dp[i][i+step] = max(max_dp[i][i+step], max_dp[i][j] + max_dp[j+1][i+step])
                        min_dp[i][i+step] = min(min_dp[i][i+step], min_dp[i][j] + min_dp[j+1][i+step])
                    elif array[c_j+1] == '-':
                        max_dp[i][i + step] = max(max_dp[i][i + step], max_dp[i][j] - min_dp[j + 1][i + step])
                        min_dp[i][i + step] = min(min_dp[i][i + step], min_dp[i][j] - max_dp[j + 1][i + step])

    return max_dp[0][length-1]


if __name__ == '__main__':
    print(solution(["1","-","3","+","5","-","8"]), 1)
    print(solution( ["5", "-", "10", "+", "1", "+", "2", "-", "4"]), -4)