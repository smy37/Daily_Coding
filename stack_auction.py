from collections import deque

def solution(prices):
    score = [0] * len(prices)

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:
                score[i] += 1
            else:
                score[i] += 1
                break

    return score