def solution(money):
    print(len(money))
    answer = 0
    case1 = [0]*len(money)
    case2 = [0]*len(money)
    for x in range(2):
        if x== 0: ## 첫번째 선택
            case1[0] = money[0]
            for i in range(len(money) -3):
                ## 두칸 뛰기
                if case1[i] + money[i+2] > case1[i+2]:
                    case1[i+2] = case1[i] + money[i+2]
                ## 세칸 뛰기
                if case1[i] + money[i+3] > case1[i+3]:
                    case1[i+3] = case1[i] + money[i+3]

        elif x == 1: ## 두번째 선택

            case2[1] = money[1]
            for i in range(1, len(money) - 3):
                print(case2)
                ## 두칸 뛰기
                if case2[i] + money[i + 2] > case2[i + 2]:
                    case2[i + 2] = case2[i] + money[i + 2]
                ## 세칸 뛰기
                if case2[i] + money[i + 3] > case2[i + 3]:
                    case2[i + 3] = case2[i] + money[i + 3]
            case2[len(money)-1] = max(case2[len(money)-1], case2[len(money)-3] + money[len(money)-1])
    print('####')
    print(case1)
    print(case2)
    answer = max(max(case1[len(money)-2], case1[len(money)-3]), max(case2[len(money)-1], case2[len(money)-2]))

    return answer


if __name__ == "__main__":
    money = [1, 2, 3, 1, 4, 5, 3, 2, 8]
    print(solution(money))